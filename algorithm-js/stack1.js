// 실버4 https://www.acmicpc.net/problem/10828

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, ...commands] = input;

const stack = [];
let results = '';

const stackCommands = {
    'push': (number) => {
        stack.push(number);
    },
    'pop': () => {
        const popedNumber = stack.pop();
        if (popedNumber) {
            return popedNumber;
        } else {
            return -1;
        }
    },
    'size': () => {
        return stack.length;
    },
    'empty': () => {
        const size = stack.length;
        return size ? 0 : 1;
    },
    'top': () => {
        const size = stack.length;
        return size ? stack[size - 1] : -1;
    }
};

for (let i = 1; i <= n; i++) {
    const [command, number] = commands[i - 1].split(' ');
    if (command.includes('push')) {
        stackCommands[command](number);
    } else {

        const result = stackCommands[command]();
        results += result + '\n';
    }
}

console.log(results);