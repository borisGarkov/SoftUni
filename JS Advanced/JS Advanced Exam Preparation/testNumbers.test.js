const { testNumbers } = require('./testNumbers');
const { expect, assert } = require('chai');

describe('Test function', () => {
    it('test num1 is not number and return undefined', () => {
        assert.equal(undefined, testNumbers.sumNumbers('1', 1));
    });

    it('test num2 is not number and return undefined', () => {
        assert.equal(undefined, testNumbers.sumNumbers(1, '1'));
    });

    it('test num1 and num2 are valid numbers and return sum', () => {
        assert.equal(2.00, testNumbers.sumNumbers(1, 1));
    });

    it('test num1 and num2 are valid floating numbers and return sum', () => {
        assert.equal(2.25, testNumbers.sumNumbers(1.125, 1.122));
    });

    it('test num1 and num2 are valid floating numbers and return round down sum', () => {
        assert.equal(2.24, testNumbers.sumNumbers(1.122, 1.122));
    });

    it('test num1 and num2 are valid negative numbers and return sum', () => {
        assert.equal(-2, testNumbers.sumNumbers(-1, -1));
    });

    it('test numberChecker fn invalid input throws error', () => {
        assert.throw(() => testNumbers.numberChecker('one'), 'The input is not a number!')
    })

    it('test numberChecker fn valid odd number expected -> \'The number is odd!\';', () => {
        assert.equal(testNumbers.numberChecker(1), 'The number is odd!');
    });

    it('test numberChecker fn valid odd negative number expected -> \'The number is odd!\';', () => {
        assert.equal(testNumbers.numberChecker(1), 'The number is odd!');
    });

    it('test numberChecker fn valid even number expected -> \'The even is odd!\';', () => {
        assert.equal(testNumbers.numberChecker(2), 'The number is even!');
    });

    it('test numberChecker fn valid even negative number expected -> \'The even is odd!\';', () => {
        assert.equal(testNumbers.numberChecker(-2), 'The number is even!');
    });

    it('test averageSumArray fn valid', () => {
        assert.equal(testNumbers.averageSumArray([2, 2, 2]), 2);
    });
})