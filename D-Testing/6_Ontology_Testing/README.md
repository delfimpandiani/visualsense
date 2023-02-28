# Ontology Testing

The eXtreme Design provides a precise methodology for testing which includes three types of tests that need to be conducted: (1) Competency question verification, (2) Inference verification, and (3) Error provocation. Competency question verification consists in the reformulation of the competency questions from natural language to SPARQL queries and running them against the ontology using a toy dataset which is supposed to include the expected result of the query. Inference verification tests are used to understand how the information needs to be produced, i.e. entered explicitly as assertions or derived from other facts through inferencing. Lastly, error provocation is a stress test of the ontology to verify how the ontology reacts when it is fed with erroneous facts or boundary data. 

The protocol that is followed for each of the tests is the following: 

1. Gather requirements
2. Select requirement to be tested
3. Formulate test procedure
4. Create test case
5. Add test data
6. Determine expected result
7. Run test
8. Compare result
9. Analyze unexpected result
10. Document test
11. Iterate if neccessary. 

