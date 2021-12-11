const { mathEnforcer } = require('./task4');
const { assert } = require('chai');

describe('task 4 test function', () => {
    it('test addFive parameter is not number, expect undefined', () => {
        assert.equal(mathEnforcer.addFive('0'), undefined);
    });

    it('test addFive parameter is number, expect number + 5', () => {
        assert.equal(mathEnforcer.addFive(0), 5);
    });

    it('test addFive parameter is float number, expect number + 5', () => {
        assert.equal(mathEnforcer.addFive(0.1), 5.1);
    });

    it('test addFive parameter is negative number, expect number + 5', () => {
        assert.equal(mathEnforcer.addFive(-1), 4);
    });

    it('test subtractTen parameter is not number, expect undefined', () => {
        assert.equal(mathEnforcer.subtractTen('0'), undefined);
    });

    it('test subtractTen parameter is number, expect number + 10', () => {
        assert.equal(mathEnforcer.subtractTen(0), -10);
    });

    it('test subtractTen parameter is negative number, expect number - 10', () => {
        assert.equal(mathEnforcer.subtractTen(-1), -11);
    });

    it('test sum parameter 1 is not number, expect undefined', () => {
        assert.equal(mathEnforcer.sum('0', 1), undefined);
    });

    it('test sum parameter 2 is not number, expect undefined', () => {
        assert.equal(mathEnforcer.sum(0, '1'), undefined);
    });

    it('test sum parameters 1 and 2 is not number, expect undefined', () => {
        assert.equal(mathEnforcer.sum('0', '1'), undefined);
    });

    it('test sum parameters 1 and 2 is valid numbers, expect 0+1=1', () => {
        assert.equal(mathEnforcer.sum(0, 1), 1);
    });

    it('test sum parameters 1 and 2 is valid numbers and num 1 is negative, expect -1+1=0', () => {
        assert.equal(mathEnforcer.sum(-1, 1), 0);
    });
});