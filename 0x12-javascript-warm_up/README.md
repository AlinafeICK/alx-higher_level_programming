[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)

Why JavaScript Programming is Amazing
    - JavaScript is amazing because it enables interactive web experiences. It is versatile, running both in the browser and on the server-side with Node.js. JavaScript's popularity ensures a vast ecosystem of frameworks and libraries, making it easier to build complex applications. It supports asynchronous programming, which is essential for modern web development.

How to Run a JavaScript Script
    - You can run JavaScript in several environments:

        In a Browser: Insert the script inside <script> tags in an HTML file.
                <script>
                console.log("Hello, World!");
                </script>
        Using Node.js: Save the script in a .js file and run it using the Node.js command.
                node script.js

How to Create Variables and Constants
    Variables and constants can be created using var, let, and const.

    var: Function-scoped, can be redeclared and updated.
    javascript
    var x = 5;
    x = 10;
    let: Block-scoped, can be updated but not redeclared.
    javascript
    
    let y = 5;
    y = 10;
    const: Block-scoped, cannot be updated or redeclared.
    javascript
    
    const z = 5;

Differences Between var, const, and let
        Scope: var is function-scoped, while let and const are block-scoped.
        Reassignment: var and let can be reassigned, const cannot.
        Hoisting: var is hoisted and initialized with undefined, while let and const are hoisted but not initialized.
        Data Types Available in JavaScript
        Primitive Types: Number, String, Boolean, Null, Undefined, Symbol, BigInt.
        Objects: Object, Array, Function, Date, RegExp, etc.

How to Use the if, if ... else Statements
        if statement:
        javascript
        
        if (condition) {
        // code to be executed if condition is true
        }
        if...else statement:
        javascript
        
        if (condition) {
        // code to be executed if condition is true
        } else {
        // code to be executed if condition is false
        }

How to Use Comments
        Single-line comment:
        javascript
        
        // This is a single-line comment
        Multi-line comment:
        javascript
        
        /*
        This is a multi-line comment
        */

How to Affect Values to Variables

        Assign values to variables using the assignment operator =.

        javascript
        
        let a = 10;
        const b = "Hello, World!";

How to Use While and For Loops
        while loop:
        javascript
        
        let i = 0;
        while (i < 10) {
        console.log(i);
        i++;
        }
        for loop:
        javascript
        
        for (let i = 0; i < 10; i++) {
        console.log(i);
        }

How to Use Break and Continue Statements
        break: Exits the loop entirely.
        javascript
        
        for (let i = 0; i < 10; i++) {
        if (i === 5) break;
        console.log(i);
        }
        continue: Skips the current iteration and moves to the next.
        javascript
        
        for (let i = 0; i < 10; i++) {
        if (i === 5) continue;
        console.log(i);
        }

What is a Function and How Do You Use Functions
        A function is a block of code designed to perform a particular task.

        Function Declaration:
        javascript
        
        function greet(name) {
        return `Hello, ${name}`;
        }
        console.log(greet("Alice"));
        Function Expression:
        javascript
        
        const greet = function(name) {
        return `Hello, ${name}`;
        };
        console.log(greet("Alice"));

What Does a Function That Does Not Use Any Return Statement Return
        A function without a return statement returns undefined.

        javascript
        
        function noReturn() {
        console.log("This function has no return statement");
        }
        console.log(noReturn()); // Outputs: undefined

Scope of Variables
Global Scope: Variables declared outside any function, available anywhere.
javascript
 
var globalVar = "I'm global";
Local Scope: Variables declared inside a function or block, only accessible within that function/block.
javascript
 
function scopeTest() {
  let localVar = "I'm local";
}
Arithmetic Operators and How to Use Them
Addition: +
javascript
 
let sum = 10 + 5; // 15
Subtraction: -
javascript

let difference = 10 - 5; // 5
Multiplication: *
javascript
 
let product = 10 * 5; // 50
Division: /
javascript
 
let quotient = 10 / 5; // 2
Modulus: %
javascript
 
let remainder = 10 % 3; // 1
How to Manipulate Dictionary (Object)
Create and manipulate objects using key-value pairs.

javascript
 
let person = {
  name: "Alice",
  age: 25
};

// Accessing properties
console.log(person.name); // Alice

// Adding properties
person.gender = "female";

// Modifying properties
person.age = 26;

// Deleting properties
delete person.age;
How to Import a File
In Node.js: Use require to import modules.
javascript
 
const fs = require('fs');
In ES6 (browser and Node.js): Use import.
javascript
 
import { myFunction } from './myModule.js';
These notes cover the essential aspects of JavaScript programming, providing a foundation for further exploration and learning.


Explain further to me when you say function-scoped and blocked-scoped?
ChatGPT
Certainly! In JavaScript, the terms "function-scoped" and "block-scoped" refer to the visibility and lifetime of variables declared with different keywords (var, let, and const).

Function-Scoped
Function-scoped means that a variable declared within a function using the var keyword is only accessible within that function. The variable is not accessible outside the function, regardless of any blocks (like loops or conditionals) within the function.

Example:
javascript
 
function exampleFunction() {
  var functionScopedVar = "I'm function-scoped";
  if (true) {
    var insideBlockVar = "I'm still function-scoped";
  }
  console.log(insideBlockVar); // Accessible here
}
console.log(functionScopedVar); // ReferenceError: functionScopedVar is not defined
exampleFunction();
In this example:

functionScopedVar is declared inside exampleFunction and is accessible anywhere within that function.
insideBlockVar is declared inside an if block, but because it uses var, it is still accessible anywhere within exampleFunction.
Block-Scoped
Block-scoped means that a variable declared within a block (e.g., inside {}) using let or const is only accessible within that block. The variable is not accessible outside the block in which it is defined.

Example:
javascript
 
function exampleFunction() {
  if (true) {
    let blockScopedVar = "I'm block-scoped";
    const anotherBlockScopedVar = "I'm also block-scoped";
    console.log(blockScopedVar); // Accessible here
    console.log(anotherBlockScopedVar); // Accessible here
  }
  console.log(blockScopedVar); // ReferenceError: blockScopedVar is not defined
  console.log(anotherBlockScopedVar); // ReferenceError: anotherBlockScopedVar is not defined
}
exampleFunction();
In this example:

blockScopedVar and anotherBlockScopedVar are declared inside an if block and are only accessible within that block.
Attempting to access blockScopedVar or anotherBlockScopedVar outside of the block where they were declared results in a ReferenceError.
Summary
Function-scoped (var): Variables are accessible throughout the entire function in which they are declared, ignoring block boundaries within that function.
Block-scoped (let and const): Variables are only accessible within the block in which they are declared, and are not accessible outside of that block.
Understanding these scoping rules helps in writing more predictable and maintainable code, as it clarifies where variables can be accessed and modified.

Explain further on Hoistiing
ChatGPT
Hoisting in JavaScript
Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope (either global or function scope) during the compilation phase. This means that you can use functions and variables before they are declared in the code. However, the behavior of hoisting differs between var, let, const, and function declarations.

Hoisting with var
When a variable is declared with var, the declaration is hoisted to the top of its scope, but not the initialization. The variable is initialized with undefined until the execution reaches the line where it is assigned a value.

Example:
javascript
 
console.log(hoistedVar); // Outputs: undefined
var hoistedVar = "I am hoisted";
console.log(hoistedVar); // Outputs: "I am hoisted"
In this example, the declaration var hoistedVar; is hoisted to the top, but the assignment hoistedVar = "I am hoisted"; is not. Hence, hoistedVar is undefined when first logged.

Hoisting with let and const
Variables declared with let and const are also hoisted, but unlike var, they are not initialized with undefined. They are in a "temporal dead zone" (TDZ) from the start of the block until the declaration is encountered. Accessing them before the declaration results in a ReferenceError.

Example with let:
javascript
 
console.log(hoistedLet); // ReferenceError: Cannot access 'hoistedLet' before initialization
let hoistedLet = "I am not hoisted";
console.log(hoistedLet); // Outputs: "I am not hoisted"
Example with const:
javascript
 
console.log(hoistedConst); // ReferenceError: Cannot access 'hoistedConst' before initialization
const hoistedConst = "I am not hoisted";
console.log(hoistedConst); // Outputs: "I am not hoisted"
Hoisting with Function Declarations
Function declarations are hoisted entirely, meaning both the function's name and its definition are hoisted. This allows you to call a function before it is declared in the code.

Example:
javascript
 
hoistedFunction(); // Outputs: "I am hoisted"

function hoistedFunction() {
  console.log("I am hoisted");
}
In this example, the function declaration function hoistedFunction() { ... } is hoisted to the top, so the function can be called before its declaration in the code.

Hoisting with Function Expressions and Arrow Functions
Function expressions and arrow functions are not hoisted. If you try to call them before they are defined, you'll get a TypeError because they are treated like variables declared with let or const.

Example with Function Expression:
javascript
 
hoistedFunctionExpression(); // TypeError: hoistedFunctionExpression is not a function

var hoistedFunctionExpression = function() {
  console.log("I am not hoisted");
};
Example with Arrow Function:
javascript
 
hoistedArrowFunction(); // TypeError: hoistedArrowFunction is not a function

var hoistedArrowFunction = () => {
  console.log("I am not hoisted");
};
Summary
var: Declarations are hoisted and initialized with undefined. Accessing the variable before its declaration will yield undefined.
let and const: Declarations are hoisted but not initialized. Accessing the variable before its declaration results in a ReferenceError due to the temporal dead zone.
Function Declarations: Entire function declarations are hoisted, allowing them to be called before they appear in the code.
Function Expressions and Arrow Functions: These are not hoisted like function declarations. Accessing them before declaration results in a TypeError.
Understanding hoisting helps in writing predictable and bug-free code by clarifying the order of execution and the scope of variables and functions.