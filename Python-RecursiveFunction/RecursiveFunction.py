import json

def find_companies(data):
    companies = []

    # Рекурсивная функция для поиска компаний в файле
    def recursive_search(node):
        if 'id' in node and 'title' in node:
            companies.append((node['title'], node['id']))
        
        if 'children' in node:
            for child in node['children']:
                recursive_search(child)
    
    recursive_search(data)

    return companies

with open('new_test_hw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

result = find_companies(data)

# Выводим информацию о найденных компаниях
for title, company_id in result:
    print(f"Название компании: {title}, ID: {company_id}")
