const { chromium } = require('playwright');
const path = require('path');

const inputHtml = process.argv[2] || '문서.html';
const outputPdf = process.argv[3] || '결과.pdf';
const mermaidBundle = require.resolve('mermaid/dist/mermaid.min.js');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const htmlPath = 'file://' + path.resolve(__dirname, inputHtml);
    await page.goto(htmlPath);

    // class="mermaid" 블록이 있으면 렌더링될 때까지 기다린 뒤 PDF를 찍는다.
    const hasMermaid = await page.evaluate(() => document.querySelectorAll('.mermaid').length > 0);
    if (hasMermaid) {
        await page.addScriptTag({ path: mermaidBundle });
        await page.evaluate(() => window.mermaid.initialize({ startOnLoad: false }));
        await page.evaluate(async () => { await window.mermaid.run(); });
        await page.waitForFunction(() => {
            const blocks = document.querySelectorAll('.mermaid');
            return blocks.length > 0 && Array.from(blocks).every((el) => el.querySelector('svg'));
        }, { timeout: 15000 });
    }

    await page.pdf({ path: path.resolve(__dirname, outputPdf) });
    await browser.close();
})();
