from neo4j import GraphDatabase
def main():
    # Neo4j connection parameters
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "12345678"

    # Function to load CSV data into Neo4j
    def load_csv(url, node_label):
        query = (
            f"LOAD CSV WITH HEADERS FROM '{url}' AS row "
            f"CREATE (n:{node_label}) SET n = row"
        )
        return query

    # Load CSV files into Neo4j
    csv_file =  'https://raw.githubusercontent.com/carlaAndr/SuperNoSQL/main/superheroes.csv'
    node_label = 'Superhero'

    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        #for csv_file, node_label in zip(csv_files, node_labels):
            with driver.session() as session:
                query = load_csv(csv_file, node_label)
                session.run(query)
                
if __name__ == "__main__":
    main()