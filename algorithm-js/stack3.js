// 골드3 https://www.acmicpc.net/problem/2812
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(' ');
const inputNumbers = input[1].split('');

const stack = [];
let count = K;

inputNumbers.forEach((number) => {
    while (count > 0 && number > stack[stack.length - 1]) {
        stack.pop();
        count--;
    }
    stack.push(number);
});

console.log(stack.join(''));