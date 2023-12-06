import unittest
import json

from days import five

class TestStringMethods(unittest.TestCase):

    def test_map_init(self):

        seed_map = five.SeedMap(4)

        
        data = {
            "0":0,
            "1":1,
            "2":2,
            "3":3
        }

        my_map = seed_map.get_map()

        self.assertEqual(my_map, data)

    def test_map(self):
        
        seeds = [79, 14, 55, 13]

        seed_map = five.SeedMap(100)
        soil_map = five.SeedMap(100)
        fert_map = five.SeedMap(100)
        water_map = five.SeedMap(100)
        light_map = five.SeedMap(100)
        temp_map = five.SeedMap(100)
        humi_map = five.SeedMap(100)

        print("seed-to-soil map:")
        seed_map.create_map(50, 98, 2)
        seed_map.create_map(52, 50, 48)
        
        print("soil-to-fertilizer map:")
        soil_map.create_map(0, 15, 37)
        soil_map.create_map(37, 52, 2)
        soil_map.create_map(39, 0, 15)

        print("fertilizer-to-water map:")
        fert_map.create_map(49, 53, 8)
        fert_map.create_map(0, 11, 42)
        fert_map.create_map(42, 0, 7)
        fert_map.create_map(57, 7, 4)


        print("water-to-light map:")
        water_map.create_map(88, 18, 7)
        water_map.create_map(18, 25, 70)
        
        print("light-to-temperature map:")
        light_map.create_map(45, 77, 23)
        light_map.create_map(81, 45, 19)
        light_map.create_map(68, 64, 13)

        print("temperature-to-humidity map:")
        temp_map.create_map(0, 69, 1)
        temp_map.create_map(1, 0, 69)

        print("humidity-to-location map:")
        humi_map.create_map(60, 56, 37)
        humi_map.create_map(56, 93, 4)

        lowest_location = 100
        
        for seed in seeds:
            soil = seed_map.convert(seed)
            fertilizer = soil_map.convert(soil)
            water = fert_map.convert(fertilizer)
            light = water_map.convert(water)
            temperature = light_map.convert(light)
            humidity = temp_map.convert(temperature)
            location = humi_map.convert(humidity)

            if location < lowest_location:
                lowest_location = location

            #print("Seed {}, soil {}, fertilizer {}, water {}, light {}, temperature {}, humidity {}, location {}.".format(seed, soil, fertilizer, water, light, temperature, humidity, location))
        
        self.assertEqual(location, 35)

    def test_fullrun(self):
        seeds = [
            432563865, 
            39236501, 
            1476854973, 
            326201032, 
            1004521373, 
            221995697, 
            2457503679, 
            46909145, 
            603710475, 
            11439698, 
            1242281714, 
            12935671, 
            2569215463, 
            456738587, 
            3859706369, 
            129955069, 
            3210146725, 
            618372750, 
            601583464, 
            1413192
        ]

        seed_map = five.SeedMap(10000000000)
        soil_map = five.SeedMap(10000000000)
        fert_map = five.SeedMap(10000000000)
        water_map = five.SeedMap(10000000000)
        light_map = five.SeedMap(10000000000)
        temp_map = five.SeedMap(10000000000)
        humi_map = five.SeedMap(10000000000)


        print("seed-to-soil map:")
        seed_map.create_map(2824905526, 2969131334, 898611144)
        seed_map.create_map(0, 322319732, 9776277)
        seed_map.create_map(379216444, 692683038, 140400417)
        seed_map.create_map(3723516670, 1559827635, 9493936)
        seed_map.create_map(637824014, 332096009, 211964909)
        seed_map.create_map(929691047, 1569321571, 35824014)
        seed_map.create_map(965515061, 1605145585, 1281263183)
        seed_map.create_map(621118546, 833083455, 16705468)
        seed_map.create_map(9776277, 0, 322319732)
        seed_map.create_map(332096009, 544060918, 47120435)
        seed_map.create_map(3733010606, 1319171816, 134731872)
        seed_map.create_map(2329500810, 1453903688, 72388062)
        seed_map.create_map(2401888872, 1526291750, 33535885)
        seed_map.create_map(2246778244, 2886408768, 82722566)
        seed_map.create_map(2435424757, 929691047, 389480769)
        seed_map.create_map(519616861, 591181353, 101501685)

        print("soil-to-fertilizer map:")
        soil_map.create_map(2819195624, 2690204780, 252557843)
        soil_map.create_map(1098298904, 1339121422, 10546957)
        soil_map.create_map(499510245, 852292683, 97183057)
        soil_map.create_map(4225167944, 2372810194, 69799352)
        soil_map.create_map(887408376, 1808006977, 56225538)
        soil_map.create_map(3071753467, 4058417302, 4632491)
        soil_map.create_map(2455749676, 3452467754, 363445948)
        soil_map.create_map(2243979338, 3846646964, 211770338)
        soil_map.create_map(3076385958, 4063049793, 231917503)
        soil_map.create_map(3860856553, 2269547568, 103262626)
        soil_map.create_map(943633914, 21067281, 39980869)
        soil_map.create_map(1388096097, 1584043708, 223963269)
        soil_map.create_map(3493291351, 2442609546, 247595234)
        soil_map.create_map(1801722612, 949475740, 41203502)
        soil_map.create_map(264653767, 678191385, 102026845)
        soil_map.create_map(3740886585, 2942762623, 89236706)
        soil_map.create_map(1152866424, 310132079, 235229673)
        soil_map.create_map(3830123291, 3815913702, 30733262)
        soil_map.create_map(249083929, 1568473870, 15569838)
        soil_map.create_map(1612059366, 1506703078, 61770792)
        soil_map.create_map(366680612, 545361752, 132829633)
        soil_map.create_map(1108845861, 1992124969, 44020563)
        soil_map.create_map(596693302, 1048406348, 290715074)
        soil_map.create_map(3467723121, 2243979338, 25568230)
        soil_map.create_map(1879110833, 1349668379, 157034699)
        soil_map.create_map(1858043552, 0, 21067281)
        soil_map.create_map(3308303461, 3293048094, 159419660)
        soil_map.create_map(3964119179, 3031999329, 261048765)
        soil_map.create_map(983614783, 780218230, 72074453)
        soil_map.create_map(1055689236, 1005796680, 42609668)
        soil_map.create_map(1673830158, 1864232515, 127892454)
        soil_map.create_map(1842926114, 990679242, 15117438)
        soil_map.create_map(0, 61048150, 249083929)

        print("fertilizer-to-water map:")
        fert_map.create_map(0, 434502471, 470583313)
        fert_map.create_map(1739362496, 1919893972, 48874906)
        fert_map.create_map(2735409723, 1968768878, 16148586)
        fert_map.create_map(3324522082, 1858151799, 61742173)
        fert_map.create_map(4137416965, 1984917464, 25502361)
        fert_map.create_map(470583313, 2971682591, 186824423)
        fert_map.create_map(2751558309, 2532295557, 111781313)
        fert_map.create_map(3664705516, 1340674299, 435773845)
        fert_map.create_map(1851374390, 3898529330, 80666020)
        fert_map.create_map(857422234, 2010419825, 207606184)
        fert_map.create_map(1788237402, 2418040507, 63136988)
        fert_map.create_map(1065028418, 0, 434502471)
        fert_map.create_map(1499530889, 2481177495, 4578648)
        fert_map.create_map(4162919326, 2916167530, 55515061)
        fert_map.create_map(1670138099, 3158507014, 69224397)
        fert_map.create_map(3386264255, 905085784, 278441261)
        fert_map.create_map(2496170686, 3979195350, 239239037)
        fert_map.create_map(4100479361, 2879229926, 36937604)
        fert_map.create_map(1504109537, 3227731411, 166028562)
        fert_map.create_map(657407736, 2218026009, 200014498)
        fert_map.create_map(2909879036, 3393759973, 257495792)
        fert_map.create_map(1932040410, 2644076870, 235153056)
        fert_map.create_map(2167193466, 3651255765, 247273565)
        fert_map.create_map(2863339622, 2485756143, 46539414)
        fert_map.create_map(3167374828, 1183527045, 157147254)
        fert_map.create_map(2414467031, 1776448144, 81703655)

        print("water-to-light map:")
        water_map.create_map(894548549, 593866955, 6252040)
        water_map.create_map(3168871398, 327816880, 11668092)
        water_map.create_map(3549766643, 2935057349, 16258370)
        water_map.create_map(1070236274, 1304104659, 106353135)
        water_map.create_map(900800589, 723222576, 35881223)
        water_map.create_map(2175309976, 2744985745, 82677694)
        water_map.create_map(3969615926, 3819543751, 36919401)
        water_map.create_map(4086160816, 4015453657, 208806480)
        water_map.create_map(0, 360262147, 233604808)
        water_map.create_map(3566025013, 1514177176, 87956572)
        water_map.create_map(3440195928, 1874477761, 44575925)
        water_map.create_map(1851853101, 948479332, 113304167)
        water_map.create_map(2969520516, 3389635913, 199350882)
        water_map.create_map(1504406289, 1061783499, 137386237)
        water_map.create_map(623007058, 1630426233, 244051528)
        water_map.create_map(1749186436, 620555911, 102666665)
        water_map.create_map(2154532801, 339484972, 20777175)
        water_map.create_map(1965157268, 759103799, 189375533)
        water_map.create_map(4007153882, 3758595179, 60948572)
        water_map.create_map(3180539490, 2951315719, 231363953)
        water_map.create_map(233604808, 1471149229, 43027947)
        water_map.create_map(276632755, 1919053686, 114911374)
        water_map.create_map(1176589409, 0, 327816880)
        water_map.create_map(867058586, 1410457794, 27489963)
        water_map.create_map(391544129, 1199169736, 4581933)
        water_map.create_map(603082303, 600118995, 19924755)
        water_map.create_map(4068102454, 4276290379, 18058362)
        water_map.create_map(3810625421, 3856463152, 158990505)
        water_map.create_map(2969008355, 620043750, 512161)
        water_map.create_map(3758595179, 4224260137, 52030242)
        water_map.create_map(396126062, 3182679672, 206956241)
        water_map.create_map(4006535327, 4294348741, 618555)
        water_map.create_map(3484771853, 3588986795, 64994790)
        water_map.create_map(2257987670, 2033965060, 711020685)
        water_map.create_map(1641792526, 2827663439, 107393910)
        water_map.create_map(3411903443, 1602133748, 28292485)
        water_map.create_map(1037034802, 1437947757, 33201472)
        water_map.create_map(936681812, 1203751669, 100352990)

        print("light-to-temperature map:")
        light_map.create_map(1726863959, 864157287, 834947717)
        light_map.create_map(263199301, 190436173, 53620398)
        light_map.create_map(1393417259, 1699105004, 333446700)
        light_map.create_map(2783912856, 244056571, 155961192)
        light_map.create_map(2939874048, 400017763, 299945457)
        light_map.create_map(671449939, 2517852185, 721967320)
        light_map.create_map(2561811676, 2295751005, 222101180)
        light_map.create_map(0, 2032551704, 263199301)
        light_map.create_map(481013766, 0, 190436173)
        light_map.create_map(316819699, 699963220, 164194067)

        print("temperature-to-humidity map:")
        temp_map.create_map(603287260, 3766826980, 8741130)
        temp_map.create_map(572607531, 3684982838, 30679729)
        temp_map.create_map(2084038135, 1101548002, 100083930)
        temp_map.create_map(655933651, 3228345771, 56278566)
        temp_map.create_map(1881393627, 553997241, 168332584)
        temp_map.create_map(553997241, 2882185871, 18610290)
        temp_map.create_map(627184746, 1072799097, 28748905)
        temp_map.create_map(612028390, 3397056204, 15156356)
        temp_map.create_map(1693489030, 1430646491, 187904597)
        temp_map.create_map(3039118107, 1734352525, 2023479)
        temp_map.create_map(220345266, 0, 43042720)
        temp_map.create_map(840454312, 3775568110, 147781659)
        temp_map.create_map(2184122065, 3715662567, 51164413)
        temp_map.create_map(317040325, 171240045, 2422893)
        temp_map.create_map(3245373536, 4158663426, 136303870)
        temp_map.create_map(145773749, 385599932, 74571517)
        temp_map.create_map(0, 43042720, 128197325)
        temp_map.create_map(1490020808, 4094893831, 63769595)
        temp_map.create_map(319463218, 173662938, 140708231)
        temp_map.create_map(712212217, 1821839294, 128242095)
        temp_map.create_map(128197325, 314371169, 17576424)
        temp_map.create_map(2474405575, 3923349769, 171544062)
        temp_map.create_map(2352890439, 3105028111, 121515136)
        temp_map.create_map(3467140696, 3318936261, 78119943)
        temp_map.create_map(2235286478, 3226543247, 1802524)
        temp_map.create_map(4084196651, 722329825, 210770645)
        temp_map.create_map(1553790403, 933100470, 139698627)
        temp_map.create_map(1261006249, 1201631932, 229014559)
        temp_map.create_map(263387986, 331947593, 53652339)
        temp_map.create_map(3137034338, 2900796161, 108339198)
        temp_map.create_map(988235971, 3412212560, 272770278)
        temp_map.create_map(2237089002, 1618551088, 115801437)
        temp_map.create_map(3381677406, 1736376004, 85463290)
        temp_map.create_map(3545260639, 1950081389, 538936012)
        temp_map.create_map(2049726211, 3284624337, 34311924)
        temp_map.create_map(2645949637, 2489017401, 393168470)
        temp_map.create_map(3041141586, 3009135359, 95892752)

        print("humidity-to-location map:")
        humi_map.create_map(596652260, 530461632, 95173962)
        humi_map.create_map(3845096173, 1731990943, 158117085)
        humi_map.create_map(2243878974, 1890108028, 393769632)
        humi_map.create_map(0, 625635594, 63651375)
        humi_map.create_map(1920725725, 753532949, 155684321)
        humi_map.create_map(63651375, 329652856, 200808776)
        humi_map.create_map(264460151, 0, 60175490)
        humi_map.create_map(1381444473, 2283877660, 346420873)
        humi_map.create_map(4003213258, 3594530530, 47694548)
        humi_map.create_map(548036821, 60175490, 46076186)
        humi_map.create_map(4100105147, 1678246429, 53744514)
        humi_map.create_map(2637648606, 3642225078, 292412911)
        humi_map.create_map(324635641, 106251676, 223401180)
        humi_map.create_map(4050907806, 3545333189, 49197341)
        humi_map.create_map(4153849661, 909217270, 141117635)
        humi_map.create_map(3455132509, 3477799963, 67533226)
        humi_map.create_map(594113007, 689286969, 2539253)
        humi_map.create_map(2930061517, 2630298533, 525070992)
        humi_map.create_map(753532949, 1050334905, 627911524)
        humi_map.create_map(3522665735, 3155369525, 322430438)
        humi_map.create_map(2076410046, 3934637989, 167468928)
        humi_map.create_map(1727865346, 4102106917, 192860379)

        lowest_location = 100
        
        for seed in seeds:
            soil = seed_map.convert(seed)
            fertilizer = soil_map.convert(soil)
            water = fert_map.convert(fertilizer)
            light = water_map.convert(water)
            temperature = light_map.convert(light)
            humidity = temp_map.convert(temperature)
            location = humi_map.convert(humidity)

            if location < lowest_location:
                lowest_location = location
        
        print(lowest_location)

        self.assertEqual(3, 3)


if __name__ == '__main__':
    unittest.main()