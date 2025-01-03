describe('template spec', () => {
  it('passes', () => {
    cy.visit('search-test.czumpers.com');

    // 1. Select the input element with name="searchText" and fill it with the "testsearch" value
    cy.get('input[name="searchText"]').type('randomtestdata');

    // 2. Select the button and click it
    cy.get('input[type="button"]').get('.searchButton').click();

    cy.wait(2000);

    const expectedNumberOfResults = 1;
    cy.get('.dataDiv').children().get("app-data-container").should('have.length', expectedNumberOfResults);

  })
})