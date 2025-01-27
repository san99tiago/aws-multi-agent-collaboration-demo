# MANUAL STEPS

These manual steps are required as these multi-agent collaboration features don't have all the necessary CDK/CloudFormation constucts/resources yet. So I will add them MANUALLY for now (this was created around the final days of 2024)...

1. Deploy with CDK.

   - `# Remember to add AWS credentials (via env-vars, config, or any other method)
   - `export AWS_DEFAULT_REGION=us-east-1`
   - `export DEPLOYMENT_ENVIRONMENT=dev`
   - `cdk deploy --require-approval never`

2. Sync the Bedrock Knowledge bases.

   - This can be done with a CustomResource, or manually by clicking the "sync" option in the KBs.

3. Update the Bedrock Agents as follows:

   - Create/Update the Bedrock Supervisor agent with the name `multi-agent-collab-demo-supervisor-v0`.
   - Update the description as: `You are a specialized SUPERVISOR agent that is able to collaborate with the <user-products-agent> (for questions related to existing user products). When a customer asks for recommended products, FIRST make sure to have <user_id> and run the <user-products-agent> and from the returned products, INFER his risk_profile, always make a choice from [CONSERVATIVE, MODERATE, RISKY], SECOND run the <financial-assistant-agent> to find the recommended product based on the risk_profile. - When a tool fetches results, always format and include them in your final response within <answer> </answer> tags. Use a clear and structured format for readability. Provide the answer in SPANISH and don't repeat question`
   - Enable the `Multi-agent collaboration` option in the Supervisor Agent with `Supervisor` option.
   - Then add collaborators as follows:
   - Select the `multi-agent-collab-demo-agent-financial-products-v0`, and add these details:
     - name: `agent-financial-products`
     - Collaborator instruction: `You can invoke this agent for information and actions related to the user's financial products.`
     <!-- - Collaborator instruction: `You can invoke this agent for information and actions related to the user's financial products. In case that products operations are requested, they must provide the <user_id> parameter, so that you can obtain all the bank products of the user. Always answer in the same language as the user asked. Never give back additional information than the one requested (only the corresponding user products).` -->
     - Click on: `Enable conversation history sharing`
   - Select the `multi-agent-collab-demo-agent-financial-assistant-v0`, and add these details:
     - name: `agent-financial-assistant`
     - Collaboration instruction: `You can invoke this agent for information and actions related to FINANCIAL ADVICE for the user and WHICH products he can obtain from the bank. Invoke this agent for Market Insights and customized recommendations for the user and the bank offerings.`
     <!-- - Collaboration instruction: `You can invoke this agent for information and actions related to FINANCIAL ADVICE for the user and WHICH products he can obtain from the bank. In case that product details are requested, they must provide the <risk_profile> parameter. Invoke this agent for Market Insights and customized recommendations for the user and the bank offerings.` -->
     - Click on: `Enable conversation history sharing`

4. Add sample data for the demo:
   - Locally execute the python files as follow:
     - `

TESTING:

- Execute: `Hola, soy "santi123" y quiero saber recomendaciones de diferentes productos?`
- Execute: `Hola, soy "dani456" y quiero saber recomendaciones de diferentes productos?`
