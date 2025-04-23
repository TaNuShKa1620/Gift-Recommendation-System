-- Create the gifts table
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gift_name TEXT NOT NULL,
    age_group TEXT NOT NULL,
    interest TEXT NOT NULL,
    image_path TEXT NOT NULL,
    price TEXT,
    link TEXT
);

-- Insert gift entries
INSERT INTO gifts (gift_name, age_group, interest, image_path, price, link) VALUES
('Crayola Inspiration Art Case', 'Child (0-12)', 'Toys', 'https://i.pinimg.com/originals/d5/52/dd/d552ddf0105ffec8f66aea22efcc5a8e.png', '₹1,599', 'https://www.amazon.in/dp/B00CI6J5JQ'),
('Snap Circuits Jr.', 'Child (0-12)', 'Gadgets', 'https://m.media-amazon.com/images/I/81S3JzwRukL._AC_SL1500_.jpg', '₹2,199', 'https://www.amazon.in/dp/B00008BFZH'),
('Harry Potter Box Set', 'Teen (13-19)', 'Books', 'https://th.bing.com/th/id/OIP.zm7B_FxYgLj-3E8ZimRjnwHaEU?rs=1&pid=ImgDetMain', '₹3,200', 'https://www.amazon.in/dp/1408856778'),
('DIY Candy Making Kit', 'Child (0-12)', 'Sweets', 'https://m.media-amazon.com/images/I/71e4l4bfQpL._AC_.jpg', '₹850', 'https://www.amazon.in/dp/B09N3Y1WSL'),
('Digital Drawing Tablet', 'Teen (13-19)', 'Gadgets', 'https://m.media-amazon.com/images/I/61+k20KQW4L._SL1500_.jpg', '₹2,999', 'https://www.amazon.in/dp/B07R9T9ZL3'),
('Fashion Watch', 'Adult (20-40)', 'Fashion', 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=60', '₹2,499', 'https://www.amazon.in/dp/B07HGG85HL'),
('Fresh Flower Bouquet', 'Adult (20-40)', 'Flowers', 'https://plus.unsplash.com/premium_photo-1676475964992-6404b8db0b53?w=600&auto=format&fit=crop&q=60', '₹499', 'https://www.amazon.in/dp/B08LGZB6XK'),
('Luxury Dark Chocolate Box', 'All', 'Sweets', 'https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&auto=format&fit=crop&q=60', '₹1,499', 'https://www.amazon.in/dp/B083Q8J1SR'),
('Ikigai: The Japanese Secret to a Long and Happy Life', 'Senior (40+)', 'Books', 'https://images.unsplash.com/photo-1588776814546-ec7fd7cbb53c?w=600&auto=format&fit=crop&q=60', '₹399', 'https://www.amazon.in/dp/178633089X'),
('Celebration Gift Hamper', 'All', 'Sweets', 'https://images.unsplash.com/photo-1609250292063-e5da25ff67e3?w=600&auto=format&fit=crop&q=60', '₹1,999', 'https://www.amazon.in/dp/B09V5FSV6P'),
('Elegant Pendant Necklace', 'Adult (20-40)', 'Fashion', 'https://images.unsplash.com/photo-1611080626919-ded0fbb63852?w=600&auto=format&fit=crop&q=60', '₹1,799', 'https://www.amazon.in/dp/B09JEWELRY'),
('Luxury Perfume Set', 'Adult (20-40)', 'Fragrance', 'https://images.unsplash.com/photo-1612277794278-70f9f1a9c67f?w=600&auto=format&fit=crop&q=60', '₹2,299', 'https://www.amazon.in/dp/B09NXYZXYZ');


