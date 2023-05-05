// 실버2 https://www.acmicpc.net/problem/10799
const input = require('fs').readFileSync('/dev/stdin').toString().trim();

const stickWithRazer = input.split('');
const stack = [];
let count = 0;

for (let i = 0; i < stickWithRazer.length; i++) {
    if (stickWithRazer[i] === '(') {
        stack.push(stickWithRazer[i]);
    } else {
        if (stickWithRazer[i - 1] === '(') {
            stack.pop();
            count += stack.length;
        } else {
            stack.pop();
            count += 1;
        }
    }
}
console.log(count);