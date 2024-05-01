Deliverables:

Shataydrian Marshall- Git Hooks for Security Static Analysis (4a)
<img width="1063" alt="Screenshot 2024-04-30 at 7 27 09 PM" src="https://github.com/symarshall42/Final-Four-Spring2024-SQA/assets/74739141/a91e9144-0aeb-4e00-a35a-8a35b42139fb">

https://github.com/symarshall42/Final-Four-Spring2024-SQA/blob/main/report.csv

In the above image I have edited a python file - fuzz.py. This image shows the git hook running on the python file and generating an output report.csv
The Git Hook is running the Bandit Software suite on each python file. 

Shataydrian Marshall- Simplistic White-box Fuzzing (4b)

The fuzz.py file is the main file. It generates the output.csv
https://github.com/symarshall42/Final-Four-Spring2024-SQA/blob/main/output.csv
https://github.com/symarshall42/Final-Four-Spring2024-SQA/blob/main/fuzz.py

Alden Snajder- SQA-LOGGER.log (4c)

Blake Anderson- SQA-CONTINUOUS-INTEGRATION.log  (4d)

What we learned:
Alden - When I was looking over the different python files, I realized the true importance that forensics has in producing accurate results from a model. In a project this size, it is important to incorporate forensics and logs in order to keep track of what inputs are going into which functions and the outputs that are produced. It helps when trying to figure out where a program encounters an error and why that error occurred. I added forensics to the report.py file because I thought it was important to log what files were getting put into the report so that the outputs would be based on the correct data. 

Blake - I implemented continuous integration with GitHub Actions. Integrating Codacy into our CI pipeline provided immediate feedback on code quality issues, allowing us to address them early in the development process. This helped in maintaining a high standard of code quality and reducing technical debt. Codacy offers a wide range of code quality checks out of the box. However, customizing these checks to suit our specific project requirements was crucial. We learned to fine-tune the Codacy configuration to focus on the most relevant issues for our codebase.

Shataydrian Marshall - I learned that there are 3 different types of git hooks which are pre-commit hook, pre-received hooks, and post-received hooks. I also now understand the importance of defense measure to protect the software and minimize vulnerabilites. Next, in white box testing the goal is to intentionally try to find vulnerabilities before your attacker does. This is a cruical step in security analysis. This project has helped me have a better understanding of how SQA tools function.
