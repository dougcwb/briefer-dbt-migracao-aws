from faker import Faker
from datetime import date
import random

fake = Faker(['pt_BR'])
# create list to store SQL statements
sqls = []
total_range = 500
# generate fake data and create INSERT SQL statements
#email, data, valor, quantidade, produto
for i in range(total_range): 
    email = fake.email()
    data = fake.date_between_dates(date_start=date.fromisoformat('2020-09-01'), date_end=date.fromisoformat('2020-09-25'))
    valor = fake.pyfloat(left_digits=6, right_digits=2, positive= True, min_value=200, max_value=99000)
    quantidade = fake.pyint(min_value=0, max_value=300)
    produto = random.choice(['Gemini', 'ChatGPT', 'Llama3.0'])
    sql = "INSERT INTO public.vendas (email, data, valor, quantidade, produto) VALUES ('{}', '{}', '{}', '{}', '{}');".format(email, data, valor, quantidade, produto)
    sqls.append(sql)

# write SQL statements to file in /tmp directory
with open(r'insert.sql', 'w') as f:
    for i, sql in enumerate(sqls):
        f.write(sql + '\n')
        print('Inserted record {} of 100'.format(i + 1))