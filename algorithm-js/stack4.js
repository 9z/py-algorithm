// 실버4 https://www.acmicpc.net/problem/9012
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, ...inputStrings] = input;

inputStrings.forEach(inputString => {
    const stack = [];
    let end = false;

    for (let i = 0; i < inputString.length; i++) {
        if (inputString[i] === '(') {
            stack.push(inputString[i]);
        } else {
            if (stack.length === 0) {
                end = true;
                console.log('NO');
                break;
            } else {
                stack.pop();
            }
        }

    }

    if (!end) {
        if (stack.length === 0) {
            console.log('YES');
        } else {
            console.log('NO');
        }
    }
});
