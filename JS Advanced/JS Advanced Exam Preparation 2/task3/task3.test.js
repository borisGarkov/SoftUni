const { library } = require('./library');
const { assert } = require('chai');

describe('test library func', () => {
    describe('test calcPriceOfBook func', () => {
        it('test not string', () => {
            assert.throw(() => library.calcPriceOfBook(0, 2000), 'Invalid input');
        });

        it('test not interger', () => {
            assert.throw(() => library.calcPriceOfBook('test', 2000.21), 'Invalid input');
        });

        it ('test price discount', () => {
            assert.equal(library.calcPriceOfBook('test', 1980), 'Price of test is 10.00')
        })

        it ('test price discount', () => {
            assert.equal(library.calcPriceOfBook('test', 1979), 'Price of test is 10.00')
        })

        it ('test no discount', () => {
            assert.equal(library.calcPriceOfBook('test', 1981), 'Price of test is 20.00')
        })

        it ('test no discount', () => {
            assert.equal(library.calcPriceOfBook('test', 2000), 'Price of test is 20.00')
        })
    })

    describe('test findBook func', () => {
        it('empty arr', () => {
            assert.throw(() => library.findBook([], 'test'), 'No books currently available');
        });

        it('not empty arr', () => {
            assert.equal(library.findBook(['test'], 'test'), 'We found the book you want.')
        });

        it('not empty arr', () => {
            assert.equal(library.findBook(['test'], ''), 'The book you are looking for is not here!')
        });

        it('not empty arr', () => {
            assert.equal(library.findBook(['test']), 'The book you are looking for is not here!')
        });
    })

    describe('test swapSeatsInHall func', () => {
        it('test not int', () => {
            assert.throw(() => library.arrangeTheBooks('1'), 'Invalid input');
        });

        it('test not int', () => {
            assert.throw(() => library.arrangeTheBooks(-1), 'Invalid input');
        });

        it('test not int', () => {
            assert.throw(() => library.arrangeTheBooks(1.1), 'Invalid input');
        });

        it('test not int', () => {
            assert.equal(library.arrangeTheBooks(2), 'Great job, the books are arranged.');
        });

        it('test not int', () => {
            assert.equal(library.arrangeTheBooks(40), 'Great job, the books are arranged.');
        });

        it('test not int', () => {
            assert.equal(library.arrangeTheBooks(41), 'Insufficient space, more shelves need to be purchased.');
        });
    })
})