#visualizar los datos
from optparse import TitledHelpFormatter
import streamlit as st
from Data.get_data import *
from streamlit_folium import folium_static
from folium import Map,Marker
import matplotlib.pyplot as plt


st.set_page_config(
     page_title="Palmer`s Penguins",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="auto",

 )

st.sidebar.title('Choose an option')
choice=st.sidebar.selectbox(
    ' ',
    ('Home','Meet the penguins','Insights','Quiz','Contact')
)
if choice =='Home':
   
    st.title("If Danny Devito would have known!")
    st.subheader(
    """
    What information you will find in this app:
    - **Home** section where you will find basic information about data and the penguins.
    - **Meet the penguins**  A brief description of each penguins species.
    - **Insights** Results of the data collected.
    - **Quiz** to test your knowledge.
    """
    )
    st.header('Palmers Penguins')
    st.image('https://miro.medium.com/max/1248/1*xJ6_zgmEEfI2BT0sRXP5cw.png')

    st.markdown("***")  
    st.write("**The default data is provided by Palmer LTER. The data we have has observations about", len(specie_penguins().keys()), "different kinds of penguins, for the years between 2007 and 2009.**")
    st.markdown("***")




    st.markdown(
    '''
    The variables the app refers to :
    - **Species**: penguin species that are present in the dataset
    - **Culmen_length_mm / bill_length_mm**: culmen length (mm)
    - **Culmen_depth_mm / bill_depth_mm**: culmen depth (mm)
    - **Flipper_length_mm**: flipper length (mm)
    - **Body_mass_g**: body mass (g)
    - **Island**: island name
    - **Sex**: penguin sex
    '''
        )
        
  
 

if choice== 'Meet the penguins':
    st.title("Palmer`s Penguins")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(list(specie_penguins().keys())[2])
        st.image('https://upload.wikimedia.org/wikipedia/commons/b/be/Pygoscelis_papua.jpg')
        st.text('''
        Kingdom: Animalia
        Phylum:	 Chordata
        Class:	 Aves
        Order:	 Sphenisciformes
        Family:  Spheniscidae
        Genus:	 Pygoscelis
        Species: P. papua

        '''
        )


    with col2:
        st.header(list(specie_penguins().keys())[1])
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg/330px-South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg')
        st.text('''
        Kingdom: Animalia
        Phylum:	Chordata
        Class:	Aves
        Order:  Sphenisciformes
        Family: Spheniscidae
        Genus:	Pygoscelis
        Species: P. adeliae
            '''
        )
     
   
   
   
    with col3:
        st.header(list(specie_penguins().keys())[0])
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg/375px-Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg')
        st.text('''
        Kingdom:  Animalia
        Phylum:	  Chordata
        Class:	  Aves
        Order:	  Sphenisciformes
        Family:	  Spheniscidae
        Genus:	  Pygoscelis
        Species:  P. antarcticus
        '''
        )
    lista_especies= list((specie_penguins().keys())) 

    descriptions={'Gentoo': """Pingüino atractivo de tamaño mediano que rara vez se ve lejos de colonias bien conocidas. 
            La apariencia es distintiva, con "audífonos" blancos y lápiz labial naranja en el pico, 
            a diferencia de cualquier otro pingüino. El sorprendente patrón de la cabeza y el pico también 
            lo convierte en uno de los pingüinos más fáciles de identificar cuando se les ve nadando en el mar.""",


    'Adelie':'''Adélie penguins live on the Antarctic continent and on many small, surrounding coastal islands. 
    They spend the winter offshore in the seas surrounding the Antarctic pack ice.Adélies feed on tiny aquatic creatures, 
    such as shrimp-like krill, but also eat fish and squid. They have been known to dive as deep as 575 feet in search of such quarry,
    though they usually hunt in far shallower waters less than half that depth.''',    

    'Chinstrap':'''
    Instantly recognizable by the black band that gives them their name, chinstrap penguins are the most abundant penguin in the Antarctic, where they gather in massive breeding colonies.

    After spending the winter north of the sea ice, chinstraps return in late October or early November to their nest sites, usually with the same breeding partners. These colonies are on the rocky, ice-free coasts of the South Sandwich Islands, South Shetland Islands, and Antarctic continent.
    '''}

    option = st.selectbox(
        'Choose a specie to know more about',
        lista_especies,index=1,key='Choose a penguin')
    for penguin, description in descriptions.items():
        if option==penguin:
            st.write(description)












if choice=='Insights':
    #mapa
    st.header('Where do the Palmer`s Penguin live?')
    st.markdown('''
    **Dream Island** is an Antarctic island located at 64°44′S 64°14′W 1 mile southeast of Cape Monaco, off the southwest coast of Anvers Island in the Palmer Archipelago.
    Dream Island was explored by the British Naval Hydrographic Survey Unit in 1956-1957.  It was named by the United Kingdom Antarctic Place-names Committee (UK-APC) 
    because its natural features include a cave and, in the summer, a small waterfall, with moss and grassy areas.

    **Torgersen Island** is a small rocky Antarctic island located 64°46′S 64°5′W east of Litchfield Island at the entrance to Port Arthur, off the southwest coast of Anvers Island in the Palmer Archipelago, between Bonaparte and Norsel Points.
    Explored by the British FIDS in 1955, it was named by the UK-APC in honour of Torstein Torgersen, first officer of the Harbor at the end of February 1955, coming from Norsel where he had been sounding.
    
    **Biscoe Islands** are a chain of Antarctic islands, adjacent to and parallel to the west coast of the Antarctic Peninsula, slightly north of the Antarctic Circle. They lie north of Adelaide Island, from which they are separated by the Matha Strait.
    They extend for about 130 km in a NE-SW direction. They were named after John Biscoe, leader of the British expedition that explored the islands on 17-18 February 1832.

    ''' )


    m= Map()

    for isla, coord in map().items():
        Marker(coord,tooltip=isla).add_to(m)
    folium_static(m)


    #mostrar poblacion de pinguinos en cada isla. 
    st.markdown("***")
    st.markdown('''**The distribution of the species based on island in the dataset**
            \n As we can see
            Biscoe and Dream have a majority of the penguins with some of them in the Torgersen island also.''')
    st.markdown("***")
    fig, ax = plt.subplots()
    ax.bar(poblacion_islas().keys(), poblacion_islas().values())
    plt.ylabel('Specimens')
    plt.title('Penguins speciments in each island')
    st.pyplot(fig)
    fig.savefig('polacion_islas.png')

    with open("polacion_islas.png", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name='polacion_islas.pn',
                mime="image/png"
           )


#Porcentaje de especie sobre total pinguinos
    st.markdown("***")
    st.markdown('''**The distribution of the species in the dataset**\n
As we can see Adelie occupies around 44% of the total, while Gentoo has around 36%, the rest around 20% is occupied by Chinstrap''')
    st.markdown("***")

    fig, ax = plt.subplots()
    ax.pie(specie_penguins().values(), labels=specie_penguins().keys(),autopct='%.1f%%')
    plt.title('Distribution of penguins species')
    ax.axis("equal")
    st.pyplot(fig)
    fig.savefig('distrib_pingüinos.png')

    with open("distrib_sexo.png", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name='distrib_pingüinos.png',
                mime="image/png"
        )


    #mostrar distribucion por sexo
    st.markdown("***")
    st.markdown(''' As we can see we have equal distribution of males and females for Adelie and Chinstraps, while for Gentoo we have a few more males.''')
    st.markdown("***")
    fig, ax = plt.subplots()
    ax.pie(esp_sex_penguins().values(), labels=esp_sex_penguins().keys(),autopct='%.1f%%')
    plt.title('Distribution of penguins species per sex')
    ax.axis("equal")
    st.pyplot(fig)
    fig.savefig('distrib_sexo.png')

    with open("distrib_sexo.png", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name='distrib_sexo.png',
                mime="image/png"

        )
    #mostrar altura por sexo y por especie
    
    option = st.selectbox(
        'What specie would you like to know more about?',
        (specie_penguins().keys())
                        )
    st.markdown("***")
    st.markdown('''As we can see from the results on average length of the bill,males´ bill are longer than females in each species.. ''')
    st.markdown("***")


    
    fig, ax = plt.subplots()
    ax.bar(media_altura(option).keys(),media_altura(option).values())
    plt.ylabel('Culmen_length_mm')
    plt.title('Average length of the bill')
    st.pyplot(fig)
    fig.savefig(f'altura_sexo_{option}.png')

    with open("distrib_sexo.png", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name=(f'altura_sexo_{option}.png'),
                mime="image/png"
        )
   
#media peso especie

    st.markdown("***")
    st.markdown('''As we can see from the results on average Gentoo specimens are the heaviest among the three species. ''')
    st.markdown("***")

    fig, ax = plt.subplots()
    ax.bar(media_peso().keys(), media_peso().values())
    plt.ylabel('Weight(g)')
    st.pyplot(fig)
    fig.savefig('media_peso.png')

    with open("polacion_islas.png", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name='media_peso.pn',
                mime="image/png"
        )


if choice =='Quiz':
   
    st.title("Let see what have you learned")
    st.text('Here are simple questions to answer')

    st.subheader('Question 1')
    question_one = st.radio(
     "Where you can find the Dream island",
     ('Pick one','Canary island', 'Indonesian Archipielago', 'Palmer`s Archipielago')) 

    if st.button('Solution'):
        if question_one == 'Palmer`s Archipielago':
            st.write('Well done')
        
        elif question_one=='Pick one':
            st.write('Pick one otpion')
        else:
            st.write('Wrong answer, try again')
  

    st.subheader('Question 2')
    question_two = st.radio(
    "What are the three species of penguins refered in this dashboard",
    ('Pick one','Gentoo,Chinstrap,Adelie', 'Snares, Gentoo,Adelie', 'Macaroni,Emperor,African')) 

    if st.button('Solution',key=1):
        if question_two == 'Gentoo,Chinstrap,Adelie':
            st.write('Well done')
        
        elif question_two=='Pick one':
            st.write('Pick one otpion')
        else:
            st.write('Wrong answer, try again')


    st.subheader('Question 3')
    question_three = st.radio(
    "Which are the heaviest penguins?",
    ('Pick one','Gentoo','Chinstrap','Adelie')) 

    if st.button('Solution',key=2):
        if question_three == 'Gentoo':
            st.write('Well done')
        
        elif question_three=='Pick one':
            t.write('Pick one otpion')
        else:
            st.write('Wrong answer, try again')

    

if choice =='Contact':

    st.header('Contact Page')
    st.subheader(' If you have any feedback or doubt please reach us filling the form below')

    contact_form='''
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type='hidden' name='_captcha' value=false>
        <input type="text" name="name" placeholder='Your name' required>
        <input type="email" name="email"  placeholder='Your email' required>
        <textarea name="message" placeholder="your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    '''
    st.markdown(contact_form,unsafe_allow_html=True)


    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

    local_css('style/style.css')