import csv
from datetime import datetime
from dateutil import relativedelta

with open("C:\\Python Project\\Contracts.csv", mode='r') as contracts_file:
    excel_reader = csv.DictReader(contracts_file)

    for row in excel_reader:
        client_name = row['client_name']
        client_payment_type = row['contract_payment_type']

        client_info = []

        if client_name and client_payment_type:
            for row in excel_reader:
                if row['client_name'] == client_name and row['contract_payment_type'] == client_payment_type:
                    client_info.append(row)

            if client_info:
                contract_num = client_info[0]['contract_id']

                output_file_path = f'C:\\Python Project\\{contract_num}{client_name.lower().replace(" ", "")}_installments_schedule.csv'

                with open(output_file_path, mode='w', newline='') as csv_file:
                    header = ['installment_serial', 'installment_date', 'installment_amount', 'max_grace_date']
                    writer = csv.writer(csv_file)
                    writer.writerow(header)

                    for contract in client_info:
                        contract_start_date = datetime.strptime(contract['contract_startdate'], '%d/%m/%Y')
                        contract_end_date = datetime.strptime(contract['contract_enddate'], '%d/%m/%Y')
                        contract_total_fees = int(contract['contract_total_fees'])

                        if contract['contract_deposit_fees']:
                            contract_deposit_fees = int(contract['contract_deposit_fees'])
                        else:
                            contract_deposit_fees = 0.0

                        total_days = (contract_end_date - contract_start_date).days

                        def calculate_number_of_installments(payment_type, total_days):
                            if payment_type == 'ANNUAL':
                                return total_days // 365
                            elif payment_type == 'QUARTER':
                                return total_days // 90
                            elif payment_type == 'MONTHLY':
                                return total_days // 30
                            elif payment_type == 'HALF_ANNUAL':
                                return total_days // 180

                        total_installments = calculate_number_of_installments(client_payment_type, total_days)

                        def calculate_installment_amount(total_fees, total_installments, deposit_fees):
                            remaining_balance = total_fees - deposit_fees
                            return remaining_balance / total_installments

                        installment_amount = calculate_installment_amount(contract_total_fees, total_installments,
                                                                          contract_deposit_fees)
                        for i in range(total_installments):
                            if client_payment_type == 'ANNUAL':
                                installment_date = contract_start_date + relativedelta(years=i)
                            elif client_payment_type == 'QUARTER':
                                installment_date = contract_start_date + relativedelta(months=i * 3)
                            elif client_payment_type == 'MONTHLY':
                                installment_date = contract_start_date + relativedelta(months=i)
                            elif client_payment_type == 'HALF_ANNUAL':
                                installment_date = contract_start_date + relativedelta(months=i * 6)

                            def weekend_check(date):
                                return date.weekday() in [4, 5]

                            while weekend_check(installment_date):
                                installment_date = installment_date + relativedelta.relativedelta(days=1)

                            grace_period_days = int(row['max_grace_period'])
                            grace_period = relativedelta.relativedelta(days=grace_period_days)
                            max_grace_date = installment_date + grace_period

                            while weekend_check(days=grace_period_days):
                                max_grace_date = max_grace_date + relativedelta.relativedelta(days=1)

                            writer.writerow([i, installment_date.strftime('%d/%m/%Y'), installment_amount,
                                             max_grace_date.strftime('%d/%m/%Y')])
