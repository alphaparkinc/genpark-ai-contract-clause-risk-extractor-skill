from client import AiContractClauseRiskExtractorClient

def main():
    client = AiContractClauseRiskExtractorClient()
    text = 'This Master Subscription Agreement is entered into by the parties...'
    res = client.extract_risks(text, 'SaaS_MSA')
    print('Contract Type: ' + res['contract_type'])
    print('Overall Risk Score: ' + str(res['overall_risk_score']) + '/100')
    print('Recommended Action: ' + res['recommended_action'])
    print('Risk Clauses:')
    for c in res['risk_clauses_found']:
        print('  [' + c['risk_level'] + '] ' + c['clause'] + ': ' + c['issue'])
        print('    Fix: ' + c['recommendation'])

if __name__ == '__main__':
    main()
