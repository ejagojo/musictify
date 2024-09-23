import streamlit.components.v1 as components

def render_carousel(data, carousel_title):
    """
    Renders a carousel for album covers or artist images using Slick Carousel.
    
    :param data: List of dictionaries with information, including 'image_url', 'name', and 'subtitle' (for artists or tracks)
    :param carousel_title: The title of the carousel to differentiate between tracks and artists
    """
    
    # Begin building the carousel HTML with required CSS and JS
    carousel_html = f"""
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"/>

    <style>
        .slick-prev:before, .slick-next:before {{
            color: black !important;  /* Explicitly define the color for the arrow buttons */
        }}
        .carousel-container {{
            margin: 0 auto;
            width: 80%;
        }}
        .slick-slide img {{
            width: 150px;
            height: 150px;
            margin: auto;
        }}
        p {{
            text-align: center;
            font-size: 14px;
            color: white !important; /* Set the font color to white */
        }}
    </style>

    <div class="carousel-container">
        <h3 style="color: white;">{carousel_title}</h3>  <!-- Set the title to white as well -->
        <div class="slider">
    """

    # Loop through data and create each slide for the carousel
    for item in data:
        carousel_html += f"""
        <div>
            <img src="{item['image_url']}" alt="Image">
            <p>{item['name']}<br>{item['subtitle']}</p>
        </div>
        """

    # Close the HTML divs
    carousel_html += """
        </div>
    </div>

    <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            $('.slider').slick({
                dots: true,
                infinite: true,
                speed: 300,
                slidesToShow: 3,
                slidesToScroll: 3,
                autoplay: true,
                autoplaySpeed: 2000,
            });
        });
    </script>
    """

    # Render the carousel using Streamlit components
    components.html(carousel_html, height=400)
