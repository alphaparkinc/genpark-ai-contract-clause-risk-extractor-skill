class AiContractClauseRiskExtractorClient:
    def extract_risks(self, contract_text='', contract_type='SaaS_MSA'):
        clauses = [
            {'clause': 'Liability Cap', 'risk_level': 'HIGH', 'issue': 'Cap set at 1x monthly fee -- insufficient for enterprise data breach exposure.', 'recommendation': 'Negotiate to 12x monthly or $1M minimum.'},
            {'clause': 'Auto-Renewal', 'risk_level': 'MEDIUM', 'issue': '30-day cancellation window with 60-day notice required -- mismatched.', 'recommendation': 'Align cancellation notice to 30 days before renewal.'},
            {'clause': 'IP Ownership', 'risk_level': 'LOW', 'issue': 'Vendor retains rights to anonymized usage data for model training.', 'recommendation': 'Add data processing addendum restricting model training use.'}
        ]
        return {
            'contract_type': contract_type,
            'risk_clauses_found': clauses,
            'overall_risk_score': 72.3,
            'recommended_action': 'NEGOTIATE_BEFORE_SIGNING'
        }
