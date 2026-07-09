const { chromium } = require('playwright');
const path = require('path');

const inputHtml = process.argv[2] || '문서.html';
const outputPdf = process.argv[3] || '결과.pdf';

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const htmlPath = 'file://' + path.resolve(__dirname, inputHtml);
    await page.goto(htmlPath);
    await page.pdf({ path: path.resolve(__dirname, outputPdf) });
    await browser.close();
})();
