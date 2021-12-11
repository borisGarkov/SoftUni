const { expect, assert } = require('chai')
const { isOddOrEven } = require('./task2')

describe('Test isOddOrEven', () => {
    it('type different from string expect undefined', () => {
        assert.equal(isOddOrEven(12), undefined);
    });

    it('len even str, expect to return even', () => {
        assert.equal(isOddOrEven('test'), 'even');
    })

    it('len odd str, expect to return odd', () => {
        assert.equal(isOddOrEven('tests'), 'odd');
    })

    it('two strings passed to the function, expect even/odd to happen', () => {
        assert.equal(isOddOrEven('test', 'test1'), 'even');
        assert.equal(isOddOrEven('test1', 'test1'), 'odd');
    })
});