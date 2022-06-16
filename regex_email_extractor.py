import re
# import requests


str = '''Designed as an urban oasis located in the heart of Central, the 111-keys hotel boasts six stunning restaurants and bars including the two-Michelin-starred Amber restaurant and the three-Michelin-starred Sushi Shikon. The Hotel is a pioneer in sustainability and advocates ethical sourcing and the removal of single-use plastic. In addition, the Hotel’s exceptional speciality suites ae perfect for designer showcase, product launches and other celebrations.
Map
The Landmark, 15 Queen’s Road Central, Hong Kong
Emaillmhkg-reservations@mohg.com
Phone+852 2132 0188
PDFHotel E-brochure
The Landmark
15 Queen’s Road Central
Hong Kong
Map & Directions
Telephone 	+852 2132 0188
Email 	lmhkg-enquiry@mohg.com
Reservations
Telephone 	+852 2132 0088
Email 	lmhkg-reservations@mohg.com
Sales & Marketing
Telephone 	+852 2132 0038
Email 	lmhkg-sales@mohg.com
Catering
Telephone 	+852 2132 0188
Email 	lmhkg-sales@mohg.com
Public Relations
Telephone 	+852 2132 0086
Email 	lmhkg-pr@mohg.com
Human Resources
Email 	lmhkg-hr@mohg.com
Spa & Wellness
Phone 	+852 2132 0011
Email 	lmhkg-spa@mohg.com
Restaurants
Amber 	 
Telephone 	+852 2132 0066
Email 	lmhkg-restaurants@mohg.com
SOMM 	 
Telephone 	+852 2132 0055
Email 	lmhkg-restaurants@mohg.com
MO Bar 	 
Telephone 	+852 2132 0077
Email 	lmhkg-restaurants@mohg.com
PDT 	 
Telephone 	+852 2132 0110
Email 	lmhkg-restaurants@mohg.com
Sushi Shikon 	 
Telephone 	+852 2643 6800
Email 	reservations@sushi-shikon.com
Kappo Rin 	 
Telephone 	+852 2643 6811
Subscribe
Sign up to receive the latest news and special offers from The Landmark Mandarin Oriental.'''

#if you want to extract emails from webite then use bellow two line of codes
# url = "https://www.mandarinoriental.com/hong-kong/the-landmark/luxury-hotel/contact-information"
# data = requests.get(url).text

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str)
print(email)