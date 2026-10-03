"""
Quiz Database for Tourism Guide Professional Certification
Modules 1 to 5 with Trilingual Explanations
"""

QUIZ_QUESTIONS = [
    # MÓDULO 1
    {
        "id": 1,
        "module": 1,
        "category": "Comunicação & Registo",
        "question_pt": "Durante uma visita guiada com turistas de várias nacionalidades, qual é a formulação mais profissional e diplomática para pedir pontualidade no ponto de encontro?",
        "question_en": "During a guided tour with international guests, which is the most professional and diplomatic phrasing to request punctuality at the meeting point?",
        "question_es": "¿Durante una visita guiada con turistas internacionales, cuál es la formulación más profesional y diplomática para solicitar puntualidad en el punto de encuentro?",
        "options": [
            "You have to be here at 4 PM sharp or the bus leaves without you.",
            "May I kindly request everyone to reconvene at our meeting point at 4:00 PM sharp so we can proceed smoothly?",
            "Stop walking around and come back at 4:00.",
            "Everybody knows the time, do not be late."
        ],
        "correct_index": 1,
        "explanation_pt": "O uso de modais de cortesia ('May I kindly request...') e a justificação do benefício comum ('so we can proceed smoothly') mantêm a autoridade do guia com máxima elegância e hospitalidade.",
        "explanation_en": "Using polite modals ('May I kindly request...') and stating the collective benefit ensures professional authority and hospitality.",
        "explanation_es": "El uso de verbos modales de cortesía ('May I kindly request...') garantiza autoridad profesional y cordialidad."
    },
    {
        "id": 2,
        "module": 1,
        "category": "Gestão de Multidões",
        "question_pt": "Em ruas estreitas de bairros históricos como Alfama, qual é o procedimento técnico correto de posicionamento do guia?",
        "question_en": "In narrow historical alleys like Alfama in Lisbon, what is the correct technical positioning for a professional tour guide?",
        "question_es": "En calles estrechas de cascos históricos como Alfama, ¿cuál es el posicionamiento técnico correcto del guía?",
        "options": [
            "Caminhar no meio da rua sem olhar para trás.",
            "Falar de costas para o monumento enquanto bloqueia a passagem de peões.",
            "Posicionar-se num recanto ou largo, mantendo o grupo à sombra e desobstruindo a passagem dos residentes.",
            "Pedir ao grupo que se disperse e corra até ao miradouro."
        ],
        "correct_index": 2,
        "explanation_pt": "O guia deve sempre posicionar o grupo em áreas amplas (largos, recantos), encostar os visitantes ao lado desobstruído e virar o grupo de costas para a luz para evitar encandeamento.",
        "explanation_en": "The guide must position the group in wider alcoves/squares, keeping clear pedestrian flow for locals and facing the group away from direct sunlight.",
        "explanation_es": "El guía debe situar al grupo en zonas amplias sin bloquear el paso y orientar a los visitantes de espaldas al sol."
    },

    # MÓDULO 2
    {
        "id": 3,
        "module": 2,
        "category": "Enologia",
        "question_pt": "Qual é a principal distinção técnica no envelhecimento entre um Vinho do Porto 'Ruby' e um 'Tawny'?",
        "question_en": "What is the primary technical difference in the aging process between a Ruby and a Tawny Port Wine?",
        "question_es": "¿Cuál es la principal distinción técnica de crianza entre un vino de Oporto 'Ruby' y un 'Tawny'?",
        "options": [
            "O Ruby é feito com uvas brancas e o Tawny com uvas tintas.",
            "O Ruby envelhece em balseiros gigantes com pouca oxigenação preservando a fruta; o Tawny estagia em pipas de carvalho com micro-oxigenação oxidativa.",
            "O Tawny é engarrafado sem adição de aguardente vínica.",
            "O Ruby é aquecido em estufas solares e o Tawny não."
        ],
        "correct_index": 1,
        "explanation_pt": "O Ruby passa por envelhecimento redutivo (preserva a cor rubi e aromas de fruta fresca), enquanto o Tawny envelhece por oxidação em pequenas pipas de carvalho de 550L (adquire cor âmbar e notas de avelã/nozes).",
        "explanation_en": "Ruby matures in large vats with minimal oxidation preserving fruitiness; Tawny ages in small oak pipes with controlled oxidation, developing amber color and nutty aromas.",
        "explanation_es": "El Ruby madura en grandes cubas preservando la fruta; el Tawny envejece en barricas de roble oxidándose, logrando tonos ámbar y aromas a frutos secos."
    },
    {
        "id": 4,
        "module": 2,
        "category": "Intercâmbio Gastronómico",
        "question_pt": "Que prato tradicional japonês tem origem direta no hábito alimentar dos marinheiros e jesuítas portugueses do século XVI?",
        "question_en": "Which traditional Japanese dish derives directly from the culinary habits of 16th-century Portuguese sailors and Jesuit missionaries?",
        "question_es": "¿Qué plato tradicional japonés tiene origen directo en la costumbre de los navegantes y jesuitas portugueses del siglo XVI?",
        "options": [
            "Sashimi de atum",
            "Tempura (derivado dos 'peixinhos da horta' e do jejum das Têmporas)",
            "Sopa de Miso",
            "Ramen de Porco"
        ],
        "correct_index": 1,
        "explanation_pt": "Durante o período católico das Têmporas (jejuns sazonais sem carne), os portugueses fritavam feijão-verde polmeado ('peixinhos da horta'), técnica que os japoneses adotaram e batizaram de 'Tempura'.",
        "explanation_en": "During the Ember days ('Quatuor Tempora' of fasting), Portuguese friars fried battered green beans, which Japanese cooks developed into Tempura.",
        "explanation_es": "Durante las Témporas de abstinencia de carne, los portugueses freían verduras rebozadas ('peixinhos da horta'), dando origen al Tempura japonés."
    },

    # MÓDULO 3
    {
        "id": 5,
        "module": 3,
        "category": "Arquitetura Manuelina",
        "question_pt": "Quais são os motivos ornamentais mais característicos do Estilo Manuelino (Gótico Tardio Português)?",
        "question_en": "Which ornamental motifs are most characteristic of the Manueline Style (Portuguese Late Gothic)?",
        "question_es": "¿Cuáles son los motivos ornamentales más característicos del Estilo Manuelino?",
        "options": [
            "Pinturas a fresco neoclássicas e colunas dóricas gregas.",
            "Cabos e nós marítimos esculpidos na pedra, corais, esferas armilares e a Cruz da Ordem de Cristo.",
            "Cúpulas bizantinas e mosaicos dourados.",
            "Apenas gárgulas em forma de dragão chinês."
        ],
        "correct_index": 1,
        "explanation_pt": "O Manuelino (século XVI, reinado de D. Manuel I) celebra as Descobertas Marítimas através de cabos de navio, nós, troncos de carvalho, corais, esferas armilares e cruzes de Cristo esculpidos na pedra de lioz.",
        "explanation_en": "Manueline architecture commemorates the Age of Discovery through stone ropes, nautical knots, corals, armillary spheres, and Christ Crosses.",
        "explanation_es": "El Manuelino conmemora los descubrimientos marítimos con cabos esculpidos, nudos, corales, esferas armilares y la Cruz de Cristo."
    },
    {
        "id": 6,
        "module": 3,
        "category": "Património Civil e Real",
        "question_pt": "Quem foi o Rei-Consorte responsável pela conceção do Palácio Nacional da Pena em Sintra no século XIX?",
        "question_en": "Which King-Consort was responsible for designing and commissioning the eclectic Pena National Palace in Sintra in the 19th century?",
        "question_es": "¿Qué Rey Consorte fue responsable del diseño del Palacio Nacional de la Pena en Sintra en el siglo XIX?",
        "options": [
            "D. Manuel I",
            "D. Fernando II de Saxe-Coburgo-Gota (o 'Rei Artista')",
            "D. Afonso Henriques",
            "D. João V"
        ],
        "correct_index": 1,
        "explanation_pt": "D. Fernando II de Saxe-Coburgo-Gota (marido da Rainha D. Maria II), homem de grande cultura e sensibilidade artística, concebeu a Pena com o arquiteto Wilhelm Ludwig von Eschwege.",
        "explanation_en": "King-Consort Ferdinand II (husband of Queen Maria II), known as the 'Artist King', created Pena Palace as the pinnacle of European Romantic eclecticism.",
        "explanation_es": "Fernando II de Sajonia-Coburgo-Gotha ('el Rey Artista') concibió el Palacio de la Pena como cumbre del Romanticismo europeo."
    },

    # MÓDULO 4
    {
        "id": 7,
        "module": 4,
        "category": "Heráldica Municipal",
        "question_pt": "Na heráldica cívica de Portugal, o que indica uma Coroa Mural composta por 5 torres de prata?",
        "question_en": "In Portuguese civic heraldry, what does a Mural Crown with 5 silver towers signify?",
        "question_es": "En la heráldica municipal portuguesa, ¿qué indica una Corona Mural de 5 torres de plata?",
        "options": [
            "Estatuto de Capital Nacional (Lisboa)",
            "Estatuto de Cidade (City)",
            "Estatuto de Vila (Town)",
            "Estatuto de Freguesia Rural"
        ],
        "correct_index": 1,
        "explanation_pt": "5 torres de prata = Cidade (ex: Porto, Coimbra, Évora); 4 torres de prata = Vila; 3 torres de prata = Freguesia; 5 torres de OURO = Capital de Portugal (Lisboa).",
        "explanation_en": "5 silver towers = City; 4 silver towers = Town (Vila); 3 silver towers = Parish (Freguesia); 5 GOLDEN towers = Capital City (Lisbon).",
        "explanation_es": "5 torres de plata = Ciudad; 4 torres de plata = Villa; 3 torres de plata = Parroquia; 5 torres de ORO = Capital de Portugal (Lisboa)."
    },
    {
        "id": 8,
        "module": 4,
        "category": "Regras Heráldicas",
        "question_pt": "Qual é a regra fundamental de contraste de esmaltes na heráldica clássica (Rule of Tinctures)?",
        "question_en": "What is the fundamental Rule of Tinctures in classical heraldry?",
        "question_es": "¿Cuál es la regla fundamental de contraste de esmaltes en la heráldica clásica?",
        "options": [
            "Pode-se pintar qualquer elemento com qualquer cor aleatória.",
            "Nunca sobrepor metal sobre metal (ouro/prata), nem cor sobre cor (gules, azur, sinopla, sable, púrpura).",
            "Os brasões devem ter apenas animais reais.",
            "As coroas têm de ser sempre azuis."
        ],
        "correct_index": 1,
        "explanation_pt": "A regra de ouro impede a sobreposição de metal sobre metal ou cor sobre cor para assegurar contraste visual imediato à distância nos campos de batalha medievais.",
        "explanation_en": "The golden rule forbids placing metal upon metal or color upon color to guarantee high-contrast visibility at distance during medieval combat.",
        "explanation_es": "La regla prohíbe colocar metal sobre metal o color sobre color para asegurar máxima visibilidad y contraste."
    },

    # MÓDULO 5
    {
        "id": 9,
        "module": 5,
        "category": "Alianças Históricas",
        "question_pt": "Em que ano foi assinado o Tratado de Windsor entre Portugal e Inglaterra, considerado a aliança diplomática ativa mais antiga do mundo?",
        "question_en": "In what year was the Treaty of Windsor signed between Portugal and England, establishing the world's oldest active diplomatic alliance?",
        "question_es": "¿En qué año se firmó el Tratado de Windsor entre Portugal e Inglaterra, la alianza diplomática activa más antigua del mundo?",
        "options": [
            "1066",
            "1386",
            "1755",
            "1910"
        ],
        "correct_index": 1,
        "explanation_pt": "O Tratado de Windsor foi ratificado a 9 de Maio de 1386 entre D. João I de Portugal e Ricardo II de Inglaterra, na sequência da Batalha de Aljubarrota (1385).",
        "explanation_en": "The Treaty of Windsor was ratified on 9 May 1386 between King John I of Portugal and Richard II of England, sealing perpetual mutual assistance.",
        "explanation_es": "El Tratado de Windsor fue ratificado el 9 de mayo de 1386 entre Juan I de Portugal y Ricardo II de Inglaterra tras la batalla de Aljubarrota."
    },
    {
        "id": 10,
        "module": 5,
        "category": "Segunda Guerra Mundial",
        "question_pt": "Durante a II Guerra Mundial, qual era o papel estratégico e a atmosfera de Lisboa e do Estoril para a Europa?",
        "question_en": "During WWII, what was the strategic role and atmosphere of Lisbon and Estoril for Europe?",
        "question_es": "Durante la II Guerra Mundial, ¿cuál fue el papel estratégico y la atmósfera de Lisboa y Estoril para Europa?",
        "options": [
            "Era uma frente de batalha com bombardeamentos aéreos constantes.",
            "Era uma capital neutra, refúgio de mais de 100.000 refugiados e epicentro de espionagem internacional (MI6 e Abwehr).",
            "Uma colónia militar britânica fechada ao público.",
            "Um porto sem qualquer tráfego marítimo."
        ],
        "correct_index": 1,
        "explanation_pt": "Lisboa foi a grande porta de saída da Europa continental para a América, onde aristocratas, cientistas, artistas e espiões conviviam pacificamente em solo neutro (inspirando a obra 'Lisbon: War in the Shadows' de Neill Lochery e o James Bond de Ian Fleming).",
        "explanation_en": "Lisbon was the open neutral gateway to freedom for 100,000+ refugees, packed with MI6 and German spies in the Estoril, inspiring Ian Fleming's James Bond.",
        "explanation_es": "Lisboa fue el puerto neutral de escape hacia América para más de 100.000 refugiados y epicentro de espías del MI6 y la Abwehr en el Estoril."
    }
]
