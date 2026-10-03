"""
Guia Turístico Pro - Base de Dados Abrangente de Glossário Técnico Trilingue
(Português Técnico e Profissional, English, Español)
Cobreado exaustivamente os 5 Módulos com grande profundidade e extensão de texto
"""

GLOSSARY_DATA = [
    # ==========================================
    # MÓDULO 1: GENERAL ENGLISH & COMUNICAÇÃO
    # ==========================================
    {
        "module": 1,
        "category_pt": "Comunicação e Gestão de Grupo",
        "category_en": "Communication & Group Management",
        "category_es": "Comunicación y Gestión de Grupo",
        "pt": "Ponto de Encontro e Gestão de Tempo de Concentração",
        "en": "Meeting Point & Punctual Assembly Protocol",
        "es": "Punto de Encuentro y Protocolo de Concentración",
        "phonetic_en": "/ˈmiː.tɪŋ pɔɪnt ænd ˈpʌŋk.tʃu.əl əˈsem.bli ˈprəʊ.tə.kɒl/",
        "phonetic_pt": "[ˈpõ.tu dɨ ẽ.ˈkõ.tɾu i ʒɨʃ.ˈtɐ̃w̃ dɨ ˈtẽ.pu]",
        "phonetic_es": "[ˈpun.to ðe eŋ.ˈkwen.tɾo i xes.ˈtjon de ˈtjem.po]",
        "context_pt": "Procedimento formal e diplomático em que o guia estabelece uma referência visual inconfundível (ex: estátua, fonte, pórtico) e determina o horário exato de reagrupamento, explicando os benefícios de pontualidade para não comprometer as reservas com hora marcada nos monumentos.",
        "context_en": "Standard professional protocol whereby the guide establishes an unmistakable visual landmark and sets a strict departure deadline, diplomatically outlining the collective benefit for pre-booked time-slot palace admissions.",
        "context_es": "Protocolo profesional por el cual el guía designa una referencia visual clara y fija la hora exacta de partida, explicando diplomáticamente la importancia de cumplir con los horarios reservados en los monumentos.",
        "example_pt": "Estimados participantes, o nosso ponto de encontro oficial será exatamente junto a esta estátua equestre. Peço a gentileza de estarem todos reunidos às 15h30 impreterivelmente para garantirmos a nossa entrada prioritária sem fila.",
        "example_en": "Distinguished guests, our official meeting point will be right by this equestrian monument. May I kindly request everyone to reconvene here at 3:30 PM sharp so we can proceed directly through our priority fast-track entrance.",
        "example_es": "Estimados visitantes, nuestro punto de encuentro oficial será junto a esta estatua ecuestre. Les ruego tengan la amabilidad de reunirse aquí a las 15:30 en punto para acceder de inmediato por nuestra entrada prioritaria reservada."
    },
    {
        "module": 1,
        "category_pt": "Segurança e Terreno",
        "category_en": "Safety & Surface Awareness",
        "category_es": "Seguridad y Terreno",
        "pt": "Alerta de Segurança: Calçada Portuguesa e Superfícies Escorregadias",
        "en": "Safety Briefing: Traditional Portuguese Cobblestones & Slippery Surfaces",
        "es": "Aviso de Seguridad: Calzada Portuguesa y Superficies Resbaladizas",
        "phonetic_en": "/ˈseɪf.ti ˈbriː.fɪŋ pɔː.tʃəˈɡiːz ˈkɒb.əl.stəʊnz/",
        "phonetic_pt": "[a.ˈlɛɾ.tɐ dɨ sɨ.ɣu.ˈɾɐ̃.sɐ kaɫ.ˈsa.ðɐ puɾ.tu.ˈɣe.zɐ]",
        "phonetic_es": "[a.ˈβi.so ðe se.ɣu.ɾi.ˈðað kal.ˈθa.ða poɾ.tu.ˈɣe.sa]",
        "context_pt": "Briefing obrigatório de segurança patrimonial relativo ao piso tradicional de calcário e basalto talhado à mão (calçada portuguesa), cujo polimento natural ao longo de décadas se torna altamente escorregadio sob chuva, humidade matinal ou em declives acentuados.",
        "context_en": "Essential preventative briefing regarding handcrafted limestone and basalt pavement (Calçada Portuguesa), where decades of pedestrian wear create a polished, low-friction surface when damp or wet.",
        "context_es": "Advertencia preventiva obligatoria sobre el pavimento tradicional de caliza y basalto pulido por el tránsito peatonal, el cual resulta sumamente resbaladizo con humedad o en pendientes pronunciadas.",
        "example_pt": "Peço a vossa máxima atenção ao caminhar sobre a nossa tradicional calçada portuguesa: os blocos de calcário polido tornam-se bastante escorregadios quando húmidos, pelo que recomendo passos curtos e calçado de sola aderente.",
        "example_en": "Please exercise extra caution when walking on our traditional Portuguese mosaic cobblestones: the polished limestone pavers become remarkably slick when wet, so I advise measured steps and rubber-soled footwear.",
        "example_es": "Les ruego especial precaución al caminar sobre la calzada portuguesa tradicional: la piedra caliza pulida resulta muy resbaladiza con humedad, por lo que recomiendo pasos cortos y calzado con suela antideslizante."
    },
    {
        "module": 1,
        "category_pt": "Storytelling e Técnicas Narrativas",
        "category_en": "Storytelling & Narrative Techniques",
        "category_es": "Storytelling y Técnicas Narrativas",
        "pt": "Gancho Narrativo e Reconstrução Cénica do Terramoto de 1755",
        "en": "Narrative Hook & Dramatic Reconstruction of the 1755 Lisbon Earthquake",
        "es": "Gancho Narrativo y Reconstrucción del Terremoto de Lisboa de 1755",
        "phonetic_en": "/ˈnær.ə.tɪv hʊk ænd ˈlɪz.bən ˈɜːθ.kweɪk/",
        "phonetic_pt": "[ˈɡɐ̃.ʃu nɐ.ʁɐ.ˈti.vu tɨ.ʁɐ.ˈmɔ.tu dɨ 1755]",
        "phonetic_es": "[ˈɡan.tʃo na.ra.ˈti.βo te.re.ˈmo.to de 1755]",
        "context_pt": "Técnica de enquadramento narrativo que transporta sensorialmente o turista para o dia 1 de Novembro de 1755, demonstrando como a tríade de catástrofes (sismo, tsunami e incêndios de cinco dias) destruiu 85% de Lisboa e revolucionou o pensamento iluminista europeu de Voltaire e Kant.",
        "context_en": "Advanced narrative framing technique placing visitors into the sensory atmosphere of 1 November 1755, demonstrating how the triad of disasters (earthquake, tsunami, and week-long firestorm) wiped out 85% of the city, inspiring Voltaire and Kant.",
        "context_es": "Técnica narrativa que transporta al visitante al 1 de noviembre de 1755, explicando cómo la combinación de seísmo, tsunami e incendios devastó el 85% de Lisboa e influyó en filósofos como Voltaire y Kant.",
        "example_pt": "Imaginem-se no dia 1 de Novembro de 1755, numa radiosa manhã do Dia de Todos os Santos com milhares de velas acesas nas igrejas: em apenas seis minutos, a terra tremeu com magnitude 8.7, seguida por ondas de 12 metros que engoliram a zona ribeirinha.",
        "example_en": "Picture yourselves on November 1st, 1755, a bright All Saints' Day morning with thousands of church candles ablaze: within just six minutes, a catastrophic 8.7-magnitude tremor struck, followed by a towering 40-foot tsunami crashing into the harbor.",
        "example_es": "Imagínense el 1 de noviembre de 1755 en una mañana de Todos los Santos con miles de velas en las iglesias: en seis minutos, un seísmo de magnitud 8.7 sacudió la ciudad, seguido por un tsunami de doce metros que arrasó la ribera.",
        "module": 1
    },

    # ==========================================
    # MÓDULO 2: GASTRONOMIA & ENOLOGIA
    # ==========================================
    {
        "module": 2,
        "category_pt": "Vinhos e Terroirs Regionais",
        "category_en": "Regional Wines & Terroirs",
        "category_es": "Vinos y Terruños Regionales",
        "pt": "Região Demarcada do Douro (1756) e Paisagem em Xisto da UNESCO",
        "en": "Douro Demarcated Wine Region (1756) & UNESCO Schist Landscape",
        "es": "Región Demarcada del Duero (1756) y Paisaje de Esquisto de la UNESCO",
        "phonetic_en": "/ˈdʊə.rəʊ ˌdiː.mɑːˈkeɪ.tɪd ˈriː.dʒən juːˈnes.kəʊ ʃɪst/",
        "phonetic_pt": "[ʁɨ.ʒi.ˈɐ̃w̃ dɨ.mɐɾ.ˈka.dɐ du ˈdo.w.ɾu ˈʃiʃ.tu]",
        "phonetic_es": "[re.ˈxjon de.maɾ.ˈka.ða ðel ˈdwe.ɾo es.ˈkis.to]",
        "context_pt": "A mais antiga região vitivinícola formalmente demarcada e regulamentada do mundo, criada por alvará régio em 1756 pelo Marquês de Pombal. Caracteriza-se pelos seus solos verticais de xisto pré-câmbrico, socalcos talhados à mão com muros de pedra solta e microclima protegido pelas serras do Marão e Montemuro.",
        "context_en": "The world's oldest legally demarcated and regulated wine appellation, chartered in 1756 by the Marquis of Pombal. Renowned for its steep precambrian schist stone terraces hand-carved over centuries and shielded from Atlantic rain by the Marão mountain range.",
        "context_es": "La región vitivinícola reglamentada más antigua del mundo, fundada en 1756 por el Marqués de Pombal. Famosa por sus bancales de esquisto tallados a mano en laderas escarpadas, protegidos de la lluvia atlántica por la sierra de Marão.",
        "example_pt": "O Alto Douro Vinhateiro é um monumento vivo à engenharia humana: milhares de quilómetros de muros de xisto foram construídos à mão para segurar a terra e produzir os vinhos mais extraordinários de Portugal.",
        "example_en": "The Alto Douro Wine Region is a living testament to human dedication: thousands of miles of schist stone dry-stone terraces were carved by hand to hold the soil and produce Portugal's most celebrated wines.",
        "example_es": "El Alto Duero Vinatero es un monumento vivo a la tenacidad humana: miles de kilómetros de muros de esquisto fueron levantados a mano para contener la tierra y cultivar los vinos más prestigiosos de Portugal."
    },
    {
        "module": 2,
        "category_pt": "Enologia e Vinhos Fortificados",
        "category_en": "Enology & Fortified Wines",
        "category_es": "Enología y Vinos Fortificados",
        "pt": "Vinho do Porto Tawny vs Ruby: O Benefício e a Ciência do Envelhecimento",
        "en": "Tawny vs Ruby Port: The Fortification Process & Aging Chemistry",
        "es": "Oporto Tawny frente a Ruby: El Beneficio y la Ciencia de la Crianza",
        "phonetic_en": "/ˈtɔː.ni vɜː.səs ˈruː.bi pɔːt fɔː.tɪ.fɪˈkeɪ.ʃən/",
        "phonetic_pt": "[ˈvi.ɲu du ˈpoɾ.tu ˈtɔ.ni ˈʁu.bi bu.nɨ.ˈfi.sju]",
        "phonetic_es": "[ˈbi.no ðe o.ˈpoɾ.to ˈto.ni ˈru.βi foɾ.ti.fi.ka.ˈsjon]",
        "context_pt": "Explicação técnica do processo de fortificação ('benefício') onde a adição de aguardente vínica a 77% cessa a fermentação preservando a doçura da uva. O Ruby passa por maturação redutiva em balseiros gigantes mantendo cor e fruta fresca; o Tawny passa por oxidação controlada em pequenas pipas de carvalho de 550L ganhando tons âmbar e aromas a avelãs, nozes e figos secos.",
        "context_en": "Technical breakdown of the fortification process ('benefício') where adding 77% neutral grape spirit halts yeast fermentation to retain natural sugars. Ruby undergoes reductive aging in massive vats preserving bold fruit, while Tawny undergoes oxidative maturation in 550L oak pipes developing amber hues, toasted hazelnuts, and dried fig notes.",
        "context_es": "Explicación técnica de la fortificación ('benefício') donde la adición de aguardiente vínico neutro a 77º interrumpe la fermentación preservando los azúcares naturales. El Ruby madura en grandes cubas conservando la fruta viva, mientras que el Tawny envejece en barricas de roble de 550L oxidándose hasta adquirir tonos ámbar y aromas a frutos secos.",
        "example_pt": "A grande diferença sensorial reside na oxigenação: enquanto o Ruby mantém a intensidade de frutos vermelhos frescos, o Tawny de 20 anos respira através da madeira de carvalho, transformando-se num licor aveludado de nozes, caramelo e especiarias.",
        "example_en": "The definitive sensory distinction lies in controlled oxygen exposure: while Ruby retains youthful fresh red-berry vitality, a 20-Year-Old Tawny breathes through seasoned oak staves, evolving into a silky elixir of toasted walnuts, butterscotch, and spice.",
        "example_es": "La gran diferencia sensorial reside en la oxigenación: mientras el Ruby preserva la frescura de los frutos rojos, un Tawny de 20 años respira a través del roble, transformándose en un licor aterciopelado con notas de nueces, caramelo y especias."
    },
    {
        "module": 2,
        "category_pt": "Intercâmbio e Rota das Especiarias",
        "category_en": "Cross-Cultural Exchanges & Spice Trade",
        "category_es": "Intercambios Culturales y Ruta de las Especias",
        "pt": "Peixinhos da Horta, Tempura e o Chá das Cinco de D. Catarina de Bragança",
        "en": "Peixinhos da Horta, Japanese Tempura & Catherine of Braganza's Tea Legacy",
        "es": "Peixinhos da Horta, Tempura y el Té de Catalina de Braganza",
        "phonetic_en": "/temˈpʊə.rə ˈɒr.ɪ.dʒɪnz ænd ˈkæθ.rɪn əv brəˈɡæn.zə/",
        "phonetic_pt": "[pɐj.ˈʃĩ.ɲuʒ dɐ ˈɔɾ.tɐ kɐ.tɐ.ˈɾi.nɐ dɨ bɾɐ.ˈɡɐ̃.sɐ]",
        "phonetic_es": "[pei.ˈʃi.ɲos da ˈoɾ.ta ka.ta.ˈli.na ðe βɾa.ˈɣan.sa]",
        "context_pt": "A revolução culinária mundial operada pelas Descobertas: os marinheiros e jesuítas portugueses levaram os 'peixinhos da horta' para Nagasaki no séc. XVI dando origem ao Tempura japonês, a carne de vinha d'alhos para Goa dando origem ao Vindaloo, e a princesa D. Catarina de Bragança introduziu o ritual diário do chá na corte britânica em 1662.",
        "context_en": "The global culinary transformation sparked by Portuguese voyages: Jesuit friars introduced battered green beans to Nagasaki inspiring Japanese Tempura, garlic-wine marinades created Goan Vindaloo, and Princess Catherine of Braganza popularized afternoon tea at the British Royal Court in 1662.",
        "context_es": "La revolución gastronómica impulsada por las navegaciones portuguesas: los misioneros jesuitas llevaron las judías verdes rebozadas a Nagasaki originando el Tempura, el marinado de ajo y vino dio origen al Vindaloo en Goa, y Catalina de Braganza introdujo la costumbre del té en Inglaterra en 1662.",
        "example_pt": "Quando provarem o Tempura no Japão ou beberem um chá com leite em Londres, lembrem-se de que foram os navegadores e princesas de Portugal que criaram e difundiram essas tradições universais.",
        "example_en": "Whenever you enjoy Japanese Tempura or savor a classic afternoon tea in London, remember that Portuguese maritime pioneers and royals originally created and popularized these global traditions.",
        "example_es": "Cuando degusten un Tempura en Japón o tomen el té de la tarde en Londres, recuerden que fueron los marineros y princesas de Portugal quienes crearon y difundieron estas tradiciones mundiales."
    },

    # ==========================================
    # MÓDULO 3: ARQUITETURA & PATRIMÓNIO
    # ==========================================
    {
        "module": 3,
        "category_pt": "Estilos e Património Mundial",
        "category_en": "Styles & World Heritage",
        "category_es": "Estilos y Patrimonio Mundial",
        "pt": "Estilo Manuelino: O Gótico Marítimo e a Janela do Capítulo de Tomar",
        "en": "Manueline Style: Portuguese Maritime Gothic & The Tomar Chapterhouse Window",
        "es": "Estilo Manuelino: El Gótico Marítimo y la Ventana del Capítulo de Tomar",
        "phonetic_en": "/ˌmæn.ju.əˈliːn staɪl tuːˈmɑː ˈtʃæp.tə.haʊs ˈwɪn.dəʊ/",
        "phonetic_pt": "[ɨʃ.ˈti.lu mɐ.nwe.ˈli.nu ʒɐ.ˈnɛ.lɐ du kɐ.ˈpi.tu.lu]",
        "phonetic_es": "[es.ˈti.lo ma.nwe.ˈli.no ben.ˈta.na ðel ka.ˈpi.tu.lo]",
        "context_pt": "Estilo arquitetónico monumental e exclusivo de Portugal, nascido no reinado de D. Manuel I (1495-1521). Funde a estrutura do gótico tardio europeu com uma iconografia profusa inspirada nas viagens oceânicas: cordas torcidas, nós de escota, corais, algas, alcachofras, cruzes de Cristo e esferas armilares esculpidas em pedra de lioz.",
        "context_en": "A monumental and uniquely Portuguese architectural style flourishing under King Manuel I (1495-1521). It merges Late European Gothic with opulent oceanographic stonework: twisted anchor ropes, nautical knots, corals, algae, Christ Crosses, and navigation armillary spheres carved in native Lioz limestone.",
        "context_es": "Estilo arquitectónico exclusivo y monumental de Portugal, desarrollado durante el reinado de Manuel I (1495-1521). Combina la estructura del gótico tardío con una profusa iconografía marítima: cabos esculpidos, nudos, corales, cruces de la Orden de Cristo y esferas armilares.",
        "example_pt": "A Janela do Capítulo no Convento de Cristo em Tomar é a apoteose do Manuelino: observem como as amarras do navio e os troncos de carvalho esculpidos em pedra parecem ganhar vida sob a luz dourada do entardecer.",
        "example_en": "The Chapterhouse Window at Tomar is the ultimate triumph of Manueline art: notice how carved nautical mooring lines and oak boughs appear to pulse with life beneath the golden evening light.",
        "example_es": "La Ventana del Capítulo en el Convento de Cristo de Tomar es la apoteosis del Manuelino: observen cómo los cabos de barco y las ramas de roble esculpidos en piedra cobran vida bajo la luz dorada del atardecer."
    },
    {
        "module": 3,
        "category_pt": "Arte Sacra e Decoração Monumental",
        "category_en": "Sacred Art & Monumental Interiors",
        "category_es": "Arte Sacro y Decoración Monumental",
        "pt": "Talha Dourada Barroca e os Painéis de Azulejos do Século de Ouro",
        "en": "Baroque Gilded Woodcarving & 18th-Century Historiated Azulejo Tiles",
        "es": "Talla Dorada Barroca y Paneles de Azulejos del Siglo de Oro",
        "phonetic_en": "/ˈɡɪl.dɪd ˈwʊdˌkɑː.vɪŋ ænd ˌæz.uːˈleɪ.ʒəʊ taɪlz/",
        "phonetic_pt": "[ˈta.ʎɐ dow.ˈɾa.dɐ bɐ.ˈʁɔ.kɐ ɐ.zu.ˈlɐj.ʒuʃ]",
        "phonetic_es": "[ˈta.ʎa do.ˈɾa.ða ba.ˈro.ka a.θu.ˈle.xos]",
        "context_pt": "A perfeita simbiose estética do Barroco Joanino (século XVIII), onde o afluxo maciço de ouro das minas do Brasil permitiu revestir igrejas inteiras com escultura em madeira coberta por folha de ouro de 24 quilates, contrastando dramaticamente com milhares de azulejos historiados em azul e branco inspirados na porcelana chinesa Ming e de Delft.",
        "context_en": "The defining aesthetic symbiosis of the King John V Baroque era (18th century), where massive Brazilian gold imports financed church interiors entirely cloaked in 24k gold leaf, creating dramatic contrast against blue-and-white tile murals inspired by Ming porcelain and Delftware.",
        "context_es": "La perfecta simbiosis estética del Barroco del siglo XVIII bajo Juan V, donde el oro de Brasil financió interiores religiosos totalmente recubiertos de pan de oro de 24 quilates en contraste con azulejos historiados en azul y blanco inspirados en la porcelana Ming.",
        "example_pt": "Na Igreja de São Francisco no Porto, mais de 300 quilos de ouro cobrem a talha de anjos e folhas de acanto, criando uma ilusão de céu dourado que deslumbrava os fiéis do século XVIII.",
        "example_en": "Inside the Church of Saint Francis in Porto, over 650 pounds of gold leaf coat intricate carvings of cherubs and acanthus leaves, crafting a golden heavenly illusion that captivated 18th-century worshipers.",
        "example_es": "En la Iglesia de San Francisco de Oporto, más de 300 kilos de pan de oro recubren la talla de querubines y hojas de acanto, creando una atmósfera celestial dorada que asombraba a los fieles del siglo XVIII."
    },

    # ==========================================
    # MÓDULO 4: HERÁLDICA
    # ==========================================
    {
        "module": 4,
        "category_pt": "Heráldica Municipal e Nacional",
        "category_en": "Municipal & National Heraldry",
        "category_es": "Heráldica Municipal y Nacional",
        "pt": "As Coroas Murais de 1930 e a Decifração dos Brasões Municipais",
        "en": "The 1930 Mural Crown System & Decoding Portuguese Civic Coats of Arms",
        "es": "El Sistema de Coronas Murales de 1930 y el Descifrado de Escudos Cívicos",
        "phonetic_en": "/ˈmjʊə.rəl kraʊn ˈsɪs.təm dɪˈkəʊ.dɪŋ ˈkəʊts əv ɑːmz/",
        "phonetic_pt": "[ku.ˈɾo.ɐʃ mu.ˈɾajʃ siʃ.ˈte.mɐ dɨ 1930 bɾɐ.ˈzõj̃ʃ]",
        "phonetic_es": "[ko.ˈɾo.nas mu.ˈɾa.les sis.ˈte.ma ðe 1930 es.ˈku.ðos]",
        "context_pt": "O regulamento nacional de heráldica municipal portuguesa de 1930 estabelece que a coroa sobre o escudo indica instantaneamente o estatuto administrativo da localidade: 5 torres de ouro para Lisboa (Capital); 5 torres de prata para Cidades (Porto, Coimbra, Évora); 4 torres de prata para Vilas (Sintra, Cascais, Óbidos); e 3 torres de prata para Freguesias.",
        "context_en": "The official 1930 Portuguese municipal heraldic code dictates that the mural crown atop any shield denotes civic rank: 5 golden towers for Lisbon (Capital); 5 silver towers for Cities (Porto, Coimbra); 4 silver towers for Towns (Sintra, Cascais); and 3 silver towers for Civil Parishes.",
        "context_es": "La reglamentación heráldica municipal portuguesa de 1930 establece que la corona sobre el escudo señala el rango de la localidad: 5 torres de oro para Lisboa (Capital); 5 torres de plata para Ciudades (Oporto, Coímbra); 4 torres de plata para Villas (Sintra, Cascais); y 3 torres de plata para Parroquias.",
        "example_pt": "Reparem no brasão de Sintra: ostenta uma coroa de 4 torres de prata porque mantém orgulhosamente o seu título de Vila, enquanto o brasão de Lisboa exibe 5 torres de ouro exclusivas da capital do país.",
        "example_en": "Look at Sintra's civic shield: it proudly displays a 4-tower silver crown denoting its historical Town status, while Lisbon's coat of arms features 5 golden towers reserved exclusively for the nation's capital.",
        "example_es": "Observen el escudo de Sintra: luce una corona de 4 torres de plata porque conserva con orgullo su título de Villa, mientras que el de Lisboa muestra 5 torres de oro exclusivas de la capital de la nación."
    },
    {
        "module": 4,
        "category_pt": "Símbolos Nacionais",
        "category_en": "National Symbols",
        "category_es": "Símbolos Nacionales",
        "pt": "As Cinco Quinas, os Sete Castelos e a Esfera Armilar de Portugal",
        "en": "The Five Quinas, Seven Castles & The Portuguese Armillary Sphere",
        "es": "Las Cinco Quinas, los Siete Castillos y la Esfera Armilar de Portugal",
        "phonetic_en": "/faɪv ˈkiː.nəs ˈsev.ən ˈkɑː.səlz ɑːˈmɪl.ər.i sfɪər/",
        "phonetic_pt": "[ɐʃ ˈsĩ.ku ˈki.nɐʃ ˈsɛ.tɨ kɐʃ.ˈtɛ.luʃ ɨʃ.ˈfɛ.ɾɐ ɐɾ.mi.ˈlaɾ]",
        "phonetic_es": "[las ˈsiŋ.ko ˈki.nas ˈsje.te kas.ˈti.ʎos es.ˈfe.ɾa aɾ.mi.ˈlaɾ]",
        "context_pt": "Análise aprofundada das Armas Nacionais de Portugal: as 5 quinas azuis em cruz recordam os 5 reis mouros derrotados em Ourique (1139) e as 5 chagas de Cristo; a bordadura vermelha com 7 castelos dourados simboliza a reconquista definitiva do Algarve por D. Afonso III em 1249; e a esfera armilar de ouro de D. Manuel I representa o cosmos e a navegação planetária.",
        "context_en": "In-depth iconography of Portugal's National Arms: the 5 blue shields symbolize the 5 Moorish kings defeated at Ourique (1139) and Christ's 5 Holy Wounds; the red border with 7 gold castles represents the 1249 Reconquest of the Algarve; and King Manuel I's golden armillary sphere embodies cosmic mastery and maritime navigation.",
        "context_es": "Análisis iconográfico del Escudo de Portugal: las 5 quinas azules representan los 5 reyes moros derrotados en Ourique (1139) y las 5 llagas de Cristo; la bordura roja con 7 castillos simboliza la reconquista del Algarve en 1249; y la esfera armilar de Manuel I encarna el dominio de los mares.",
        "example_pt": "Cada elemento da nossa bandeira encerra séculos de história: as quinas nasceram nos campos de batalha medievais de D. Afonso Henriques e a esfera armilar uniu os quatro cantos do mundo durante as Descobertas.",
        "example_en": "Every symbol on our national coat of arms reflects centuries of history: the blue quinas trace back to King Afonso Henriques' medieval battlefields, while the armillary sphere joined continents during the Age of Discovery.",
        "example_es": "Cada símbolo de nuestro escudo encierra siglos de historia: las quinas azules proceden de los campos de batalla medievales de Alfonso Henriques y la esfera armilar unió los continentes durante los Descubrimientos."
    },

    # ==========================================
    # MÓDULO 5: HISTÓRIA & LAÇOS BRITÂNICOS/EUROPEUS
    # ==========================================
    {
        "module": 5,
        "category_pt": "Tratados e Alianças Históricas",
        "category_en": "Historic Treaties & Alliances",
        "category_es": "Tratados y Alianzas Históricas",
        "pt": "Tratado de Windsor de 1386: A Aliança Perpétua Mais Antiga do Mundo",
        "en": "The 1386 Treaty of Windsor: The World's Oldest Active Diplomatic Alliance",
        "es": "El Tratado de Windsor de 1386: La Alianza Diplomática Activa Más Antigua del Mundo",
        "phonetic_en": "/ˈtriː.ti əv ˈwɪn.zə ˈθɜː.tiːn eɪ.ti sɪks ˈwɜːldz ˈəʊl.dɪst əˈlaɪ.əns/",
        "phonetic_pt": "[tɾɐ.ˈta.du dɨ ˈwĩd.zɔɾ 1386 ɐ.li.ˈɐ̃.sɐ]",
        "phonetic_es": "[tɾa.ˈta.ðo ðe ˈwin.soɾ 1386 a.ˈljan.sa]",
        "context_pt": "Tratado de aliança militar e diplomática perpétua assinado a 9 de Maio de 1386 entre D. João I de Portugal e Ricardo II de Inglaterra, na sequência da Batalha de Aljubarrota (1385). Selado pelo casamento de D. João I com D. Filipa de Lencastre (mãe do Infante D. Henrique), o tratado mantém-se juridicamente em vigor há mais de 640 anos, tendo sido invocado na Guerra Peninsular, na I e II Guerras Mundiais e na Guerra das Malvinas.",
        "context_en": "Perpetual mutual defense and diplomatic pact signed on 9 May 1386 between King John I of Portugal and King Richard II of England, following the victory at Aljubarrota (1385). Sealed by the royal marriage to English Princess Philippa of Lancaster (mother of Prince Henry the Navigator), the treaty remains legally binding after 640+ years, invoked in the Peninsular War, WWI, WWII (Azores base), and the 1982 Falklands War.",
        "context_es": "Pacto militar y diplomático perpetuo firmado el 9 de mayo de 1386 entre Juan I de Portugal y Ricardo II de Inglaterra tras la batalla de Aljubarrota (1385). Sellado por el matrimonio con la princesa inglesa Felipa de Lancaster, el tratado sigue legalmente activo tras más de 640 años, habiendo sido invocado en la Guerra Peninsular, las dos Guerras Mundiales y la Guerra de las Malvinas.",
        "example_pt": "O Tratado de Windsor de 1386 é um marco incomparável no direito internacional: une Portugal e a Grã-Bretanha numa fraternidade ininterrupta que atravessou séculos de impérios, guerras e transformações globais.",
        "example_en": "The 1386 Treaty of Windsor is a unique achievement in international law: it binds Portugal and Great Britain in an unbroken alliance that has survived over six centuries of empires, global wars, and geopolitical shifts.",
        "example_es": "El Tratado de Windsor de 1386 es un hito singular en el derecho internacional: une a Portugal y Gran Bretaña en una alianza ininterrumpida que ha superado más de seis siglos de imperios y guerras mundiales."
    },
    {
        "module": 5,
        "category_pt": "Segunda Guerra Mundial e Espionagem",
        "category_en": "World War II & Espionage",
        "category_es": "Segunda Guerra Mundial y Espionaje",
        "pt": "Lisboa Neutra na II Guerra Mundial: O Santuário Europeu e o Berço de James Bond",
        "en": "Neutral Lisbon in WWII: European Sanctuary & The Birth of James Bond 007",
        "es": "Lisboa Neutral en la II Guerra Mundial: Santuario Europeo y Cuna de James Bond",
        "phonetic_en": "/ˈnjuː.trəl ˈlɪz.bən dʒeɪmz bɒnd ˈes.pɪ.ə.nɑːʒ/",
        "phonetic_pt": "[liʒ.ˈbo.ɐ ˈnew.tɾɐ ʃpi.u.ˈna.ʒɐ̃j̃ ɨʃ.tu.ˈɾiɫ]",
        "phonetic_es": "[lis.ˈβo.a new.ˈtɾal es.pjo.ˈna.xe es.to.ˈɾil]",
        "context_pt": "Entre 1939 e 1945, sob o regime de Salazar, Lisboa manteve uma rigorosa neutralidade estratégica, tornando-se o único porto marítimo e aéreo aberto da Europa continental para as Américas. Mais de 100.000 refugiados passaram pela capital portuguesa, incluindo a família real dos Habsburgos e intelectuais de renome. No Hotel Palácio e no Casino Estoril cruzavam-se espiões do MI6 britânico e da Abwehr alemã, onde o oficial de inteligência naval Ian Fleming se inspirou no agente duplo Dusko Popov para conceber o lendário James Bond em 'Casino Royale'.",
        "context_en": "Between 1939 and 1945, neutral Lisbon was the sole open sea and air gateway from Nazi-occupied Europe to the Americas. Over 100,000 refugees found safe passage through Portugal. Meanwhile, the luxury Hotel Palácio and Casino in Estoril turned into an international spy hub where British MI6 and German Abwehr operatives mingled; here, naval intelligence officer Ian Fleming observed double agent Dusko Popov, inspiring the creation of James Bond 007 in 'Casino Royale'.",
        "context_es": "Entre 1939 y 1945, Lisboa fue la única puerta marítima y aérea abierta de Europa hacia América. Más de 100.000 refugiados lograron escapar a través de Portugal. En el Hotel Palácio y el Casino de Estoril convivían espías del MI6 británico y la Abwehr alemana; allí, el oficial Ian Fleming se inspiró en el agente doble Dusko Popov para crear al mítico James Bond 007 en 'Casino Royale'.",
        "example_pt": "Durante os anos sombrios da Segunda Guerra Mundial, Lisboa era um farol de luz e liberdade na Europa: enquanto milhares de refugiados procuravam um bilhete de navio para a América, nos salões do Estoril decorria o mais fascinante jogo de espionagem secreta da história.",
        "example_en": "During the dark years of World War II, Lisbon stood as a beacon of light and refuge in Europe: while thousands sought passage across the Atlantic, the glamorous salons of Estoril hosted the most thrilling real-life intelligence chess match in history.",
        "example_es": "Durante los años de la Segunda Guerra Mundial, Lisboa fue un oasis de refugio en Europa: mientras miles buscaban un billete hacia América, en los salones de Estoril se desarrollaba la partida de espionaje más fascinante de la historia moderna."
    },
    {
        "module": 5,
        "category_pt": "História Contemporânea e Liberdade",
        "category_en": "Contemporary History & Democracy",
        "category_es": "Historia Contemporánea y Libertad",
        "pt": "A Revolução dos Cravos (25 de Abril de 1974) e a Construção da Democracia",
        "en": "The Carnation Revolution (25 April 1974) & The Dawn of Modern Portuguese Democracy",
        "es": "La Revolución de los Claveles (25 de Abril de 1974) y la Democracia Moderna",
        "phonetic_en": "/ˌkɑː.neɪ.ʃən ˌrev.əˈluː.ʃən ˈtwen.ti fɪfθ əv ˈeɪ.prəl/",
        "phonetic_pt": "[ʁɨ.vu.lu.ˈsɐ̃w̃ duʃ ˈkɾa.vuʃ 25 dɨ ɐ.ˈβɾiɫ]",
        "phonetic_es": "[re.βo.lu.ˈsjon de los kla.ˈβe.les 25 de a.ˈβɾil]",
        "context_pt": "O histórico levantamento militar pacífico conduzido pelo Movimento das Forças Armadas (MFA) que pôs fim a 48 anos de ditadura do Estado Novo. Transmitidas pela rádio as senhas secretas 'E Depois do Adeus' e 'Grândola, Vila Morena', os blindados de Salgueiro Maia ocuparam os ministérios em Lisboa sem derramar sangue. A população ofereceu cravos vermelhos aos soldados, que os colocaram nos canos das espingardas G3, transformando o cravo no símbolo universal da transição pacífica para a democracia e posterior integração europeia em 1986.",
        "context_en": "The historic peaceful military coup led by the Armed Forces Movement (MFA) ending 48 years of authoritarian Estado Novo rule. Triggered by the secret radio broadcasts of 'E Depois do Adeus' and 'Grândola, Vila Morena', Captain Salgueiro Maia's armored column bloodlessly secured Lisbon. Citizens handed red carnations to the troops, who slotted them into their rifle barrels, turning the red carnation into the universal icon of peaceful liberation and opening the path to EU integration in 1986.",
        "context_es": "El histórico levantamiento militar pacífico del Movimiento de las Fuerzas Armadas (MFA) que derrocó 48 años de dictadura del Estado Novo. Tras la emisión radiofónica de las canciones clave 'E Depois do Adeus' y 'Grândola, Vila Morena', los blindados ocuparon Lisboa sin derramamiento de sangre. El pueblo ofreció claveles rojos que los soldados colocaron en los cañones de sus fusiles, convirtiendo el clavel en el símbolo mundial de la libertad y facilitando el ingreso de Portugal en la Unión Europea en 1986.",
        "example_pt": "O 25 de Abril de 1974 é uma das mais belas páginas da história contemporânea mundial: uma revolução sem balas onde cravos vermelhos floresceram nos canos das espingardas para devolver a liberdade, os direitos cívicos e a dignidade a Portugal.",
        "example_en": "The 25th of April 1974 represents one of the most inspiring moments in modern history: a bloodless revolution where red carnations blossomed inside rifle barrels to restore democracy, human rights, and freedom to Portugal.",
        "example_es": "El 25 de abril de 1974 constituye una de las páginas más inspiradoras de la historia contemporánea: una revolución pacífica donde claveles rojos brotaron de los fusiles para devolver la libertad, la democracia y la dignidad a Portugal."
    }
]

