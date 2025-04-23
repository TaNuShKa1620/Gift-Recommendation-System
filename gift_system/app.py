from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')

# Replace these with your own MySQL database details!
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ttanu@16',
    'database': 'gifts'
}

def initialize_database():
    conn = None  # Initialize conn variable to avoid UnboundLocalError
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password']
        )
        
        if conn.is_connected():  # Check if the connection is successful
            print("Successfully connected to MySQL database!")

        cursor = conn.cursor()

        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_config['database']))
        conn.commit()

        conn.database = db_config['database']

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gifts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                gift_name VARCHAR(255),
                age_group VARCHAR(50),
                interest VARCHAR(100),
                image_path VARCHAR(255),
                price VARCHAR(50),
                link VARCHAR(255)
            )
        """)
        conn.commit()

        # Alter the 'link' column to increase its length
        cursor.execute("""
            ALTER TABLE gifts
            MODIFY link VARCHAR(1000)
        """)
        conn.commit()

        # Remove old Celebration Gift Hamper link if exists
        cursor.execute("""
            DELETE FROM gifts
            WHERE gift_name = 'Celebration Gift Hamper'
        """)
        conn.commit()

        # Insert updated Celebration Gift Hamper
        cursor.execute("""
            INSERT INTO gifts (gift_name, age_group, interest, image_path, price, link)
            VALUES (
                'Celebration Gift Hamper',
                'All',
                'Sweets',
                'https://m.media-amazon.com/images/I/61m-9zuL0xL.SX679_PIbundle-2,TopRight,0,0_AA679SH20.jpg',
                '₹3,824',
                'https://www.amazon.in/Hersheys-Exotic-Dark-Gift-Pack/dp/B08HLMR14G/ref=sr_1_10?crid=1ONZMOOJMINJX&dib=eyJ2IjoiMSJ9.06iiFsVR4pDOF-1axb5R9Wgb97uPWZBBqRxDBs-1EUJQY4j4SdhTo0oHX-ux_NFnpCZTCY8TYlLTZ54hdJTOLx8OPSrux0TgrHo9js0vVSWRXBW4-YpQPNp_6-48vovl3hvWXHdIVcRUWbmxNPooNjP8zXqTU-1m2_unGZ0fcml9tY67djkkCq-f_hBNWsquR5T6Uq7q5uT0ulSHcPMORf8QJE7KkkM-lLW0NLKfp9OyIAdMBqV9OlJCEvJQKYhvHKB3zNeXUHUxN9o4GrAP5SnGhJxCyoxDDPkaWgMv6sw.ZSBlgSSFdGD0E04drIVjZfqbhUhepgDOjRpjw0xPO5I&dib_tag=se&keywords=dark%2Bchocolate%2Bbox&qid=1744277741&s=grocery&sprefix=dark%2Bchocolate%2Bbox%2Cgrocery%2C221&sr=1-10&th=1'
            )
        """)
        conn.commit()

        # Remove old Ikigai Book and Luxury Perfume Gift Set if they exist
        cursor.execute("""
            DELETE FROM gifts
            WHERE gift_name IN ('Ikigai: The Japanese Secret to a Long and Happy Life', 'Luxury Perfume Gift Set')
        """)
        conn.commit()

        # Insert updated Ikigai Book
        cursor.execute("""
            INSERT INTO gifts (gift_name, age_group, interest, image_path, price, link)
            VALUES (
                'Ikigai: The Japanese Secret to a Long and Happy Life',
                'Senior (40+)',
                'Books',
                'https://m.media-amazon.com/images/I/81l3rZK4lnL.SY425.jpg',
                '₹354',
                'https://www.amazon.in/Ikigai-H%C3%A9ctor-Garc%C3%ADa/dp/178633089X'
            )
        """)
        conn.commit()

        # Insert updated Luxury Perfume Gift Set
        cursor.execute("""
            INSERT INTO gifts (gift_name, age_group, interest, image_path, price, link)
            VALUES (
                'Luxury Perfume Gift Set',
                'Adult (20-40)',
                'Fashion',
                'https://cdn.fcglcdn.com/brainbees/images/products/583x720/19062326a.webp',
                '₹716',
                'https://www.firstcry.com/carlton-london/carlton-london-women-dazzle-gift-set-of-4-edp-perfume-20ml-each/19062326/product-detail?ref=BSN_Shopping_78_Fragrance!BSN-Standard_All_Search_Ads!&msclkid=9635bd020b4c1bca3a08daf5834ef44c&utm_source=bing&utm_medium=cpc&utm_campaign=BSN-Standard_All_Search_Ads&utm_term=4586337882898975&utm_content=Ad%20group%20%231'
            )
        """)
        conn.commit()

        # Remove old Pendant Necklace if it exists
        cursor.execute("""
            DELETE FROM gifts
            WHERE gift_name = 'Pendant Necklace'
        """)
        conn.commit()

        # Remove old Elegant Necklace link if it exists
        cursor.execute("""
            DELETE FROM gifts
            WHERE gift_name = 'Elegant Pendant Necklace'
        """)
        conn.commit()

        # Insert updated Pendant Necklace
        cursor.execute("""
            INSERT INTO gifts (gift_name, age_group, interest, image_path, price, link)
            VALUES (
                'Pendant Necklace',
                'Adult (20-40)',
                'Fashion',
                'https://cdn.fcglcdn.com/brainbees/images/products/583x720/13353437a.webp',
                '₹1999',
                'https://www.firstcry.com/clara/clara-925-sterling-silver-gold-rhodium-plated-azrah-necklace-chain-gold/13353437/product-detail?ref=BSN_Shopping_78_Jewellery!BSN-Standard_All_Search_Ads!&msclkid=a50c1a0b4c6f1f6816ee7dfccaa8a778&utm_source=bing&utm_medium=cpc&utm_campaign=BSN-Standard_All_Search_Ads&utm_term=4586337882898975&utm_content=Ad%20group%20%231'
            )
        """)
        conn.commit()

        print("Database and table are ready.")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()

def get_filtered_gifts(age_group, interest):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Corrected the misplaced SQL query
    query = """
        SELECT gift_name, age_group, interest, image_path, price, link
        FROM gifts
        WHERE age_group = %s AND LOWER(interest) = LOWER(%s)
    """

    cursor.execute(query, (age_group, interest))
    rows = cursor.fetchall()
    conn.close()

    print("DEBUG: Filtered gifts with image URLs:")
    for row in rows:
        print(f"Gift Name: {row[0]}, Image URL: {row[3]}")

    gifts = []
    for row in rows:
        gifts.append({
            'name': row[0],
            'age_group': row[1],
            'interest': row[2],
            'image_url': row[3],
            'price': row[4],
            'buy_link': row[5]
        })

    print(f"DEBUG — Found {len(gifts)} gifts for Age Group: {age_group} & Interest: {interest}")
    return gifts

@app.route('/', methods=['GET', 'POST'])
def index():
    categories = ["Electronics", "Books", "Clothing", "Toys"]
    occasions = ["Birthday", "Anniversary", "Wedding", "Graduation"]

    if request.method == 'POST':
        age_group = request.form.get('age')
        interest = request.form.get('interest')

        print(f"Received Age Group: {age_group}, Interest: {interest}")

        if not age_group or not interest:
            return render_template('index.html', categories=categories, occasions=occasions,
                                   error="Please select both age group and interest.")

        gifts = get_filtered_gifts(age_group, interest)
        return render_template('result.html', gifts=gifts, selected_age=age_group, selected_interest=interest)

    return render_template('index.html', categories=categories, occasions=occasions)

@app.route('/recommend', methods=['POST'])
def recommend():
    age_group = request.form['age_group']
    interest = request.form['interest']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gifts WHERE age_group = %s AND interest = %s", (age_group, interest))
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            'age_group': row[1],
            'interest': row[2],
            'name': row[0],
            'image_url': row[3],
            'price': row[4],
            'buy_link': row[5]
        })

    return render_template('result.html', results=results)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        age_group = request.form.get('age_group')
        interest = request.form.get('interest')

        if not age_group or not interest:
            return render_template('index.html', error="Please select both age group and interest.")

        # Fetch results from the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT gift_name, age_group, interest, image_path, price, link
            FROM gifts
            WHERE (age_group = %s OR age_group = 'All')
            AND LOWER(interest) = LOWER(%s)
        """
        cursor.execute(query, (age_group, interest))
        rows = cursor.fetchall()
        conn.close()

        # Format results for rendering
        gifts = []
        for row in rows:
            gifts.append({
                'name': row[0],
                'age_group': row[1],
                'interest': row[2],
                'image_url': row[3],
                'price': row[4],
                'buy_link': row[5]
            })

        return render_template('result.html', gifts=gifts, selected_age=age_group, selected_interest=interest)

    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/check_db')
def check_db():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES LIKE 'gifts';")
        table_exists = cursor.fetchone()
        conn.close()

        if table_exists:
            return "Yes, the database is connected and the 'gifts' table exists."
        else:
            return "No, the 'gifts' table does not exist in the database."
    except mysql.connector.Error as e:
        return f"MySQL connection failed: {e}"

@app.route('/result', methods=['POST'])
def result():
    age_group = request.form.get('age_group')
    interest = request.form.get('interest')

    # Fetch filtered gifts based on age group and interest
    filtered_gifts = get_filtered_gifts(age_group, interest)

    # Debugging: Print filtered gifts
    print(f"Filtered gifts: {filtered_gifts}")

    return render_template('result.html', gifts=filtered_gifts, selected_age=age_group, selected_interest=interest)

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)