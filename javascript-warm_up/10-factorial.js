#!/usr/bin/node

const factorial = function (n) {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  console.log(result);
};

factorial(process.argv[2]);
