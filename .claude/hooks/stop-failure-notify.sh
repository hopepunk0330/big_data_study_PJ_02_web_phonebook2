#!/usr/bin/env bash
# StopFailure hook: rate_limit/overloaded로 턴이 끊기면 데스크톱 알림 + 로그만 남긴다.
# non-blocking 훅이라 exit code/출력은 Claude Code 동작에 영향을 주지 않는다 — 관찰용.
#
# 주의: settings.local.json의 matcher("rate_limit|overloaded")가 실제로는 걸러주지 않는
# 것이 실측으로 확인됐다(2026-07-14, error_type=unknown 이벤트도 그대로 호출됨) — 문서와
# 다르게 동작하거나 버그로 보인다. 그래서 필터링을 이 스크립트 안에서 직접 한다.

input="$(cat)"
error_type="$(printf '%s' "$input" | jq -r '.error_type // "unknown"')"
error_message="$(printf '%s' "$input" | jq -r '.error_message // ""')"
session_id="$(printf '%s' "$input" | jq -r '.session_id // ""')"

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
log_dir="$script_dir/../logs"
mkdir -p "$log_dir"
log_file="$log_dir/stop-failures.log"

timestamp="$(date '+%Y-%m-%d %H:%M:%S')"

# 모든 StopFailure 이벤트는 일단 로그에 남긴다(디버깅용) — 어떤 타입이 실제로 오는지 계속 관찰.
echo "[$timestamp] error_type=$error_type session_id=$session_id message=$error_message" >> "$log_file"

# 알림(맥 팝업 + Slack)은 rate_limit/overloaded일 때만 — matcher를 믿지 않고 여기서 직접 거른다.
case "$error_type" in
  rate_limit|overloaded) ;;
  *) exit 0 ;;
esac

safe_message="$(printf '%s' "$error_message" | sed 's/\\/\\\\/g; s/"/\\"/g')"
osascript -e "display notification \"$safe_message\" with title \"Claude Code 중단됨 ($error_type)\" sound name \"Basso\"" >/dev/null 2>&1

webhook_file="$script_dir/.slack-webhook-url"
if [ -f "$webhook_file" ]; then
  webhook_url="$(cat "$webhook_file")"
  slack_text="Claude Code 중단됨 (\`$error_type\`, $(hostname -s) — $timestamp): $error_message"
  payload="$(jq -n --arg text "$slack_text" '{text: $text}')"
  curl -s -X POST -H 'Content-type: application/json' --data "$payload" "$webhook_url" >/dev/null 2>&1
fi

exit 0
