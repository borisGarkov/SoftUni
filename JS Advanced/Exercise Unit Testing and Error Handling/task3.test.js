const { assert } = require('chai');
const { lookupChar } = require('./task3');

describe('main tests', () => {
    it('check invalid input data - not input string', () => {
        assert.equal(lookupChar(1, 2), undefined);
    });

    it('check invalid input data - not input number for index', () => {
        assert.equal(lookupChar('string', 'string'), undefined);
    });

    it('check invalid input data - index is floating number', () => {
        assert.equal(lookupChar('string', 1.5), undefined);
    });

    it('check invalid input data - index smaller than len of string', () => {
        assert.equal(lookupChar('string', -1), "Incorrect index");
    });

    it('check invalid input data - index bigger than len of string', () => {
        assert.equal(lookupChar('string', 6), "Incorrect index");
    });

    it('check valid data - both string and index', () => {
        assert.equal(lookupChar('string', 0), 's');
    });
});
