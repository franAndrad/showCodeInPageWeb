function copyCode() {
    const code = document.querySelector('.code');
    const range = document.createRange();
    range.selectNode(code);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
}
