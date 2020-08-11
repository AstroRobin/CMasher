# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'diverging'

# RGB-values of this colormap
cm_data = [[0.11138401, 0.02669949, 0.18994576],
           [0.11630584, 0.02843274, 0.19596041],
           [0.12122371, 0.03017008, 0.20200385],
           [0.12613965, 0.03190505, 0.20808061],
           [0.13105245, 0.03363619, 0.21418972],
           [0.13596355, 0.03535760, 0.22033503],
           [0.14087256, 0.03706639, 0.22651726],
           [0.14577938, 0.03875900, 0.23273789],
           [0.15068450, 0.04043075, 0.23899957],
           [0.15558810, 0.04203151, 0.24530468],
           [0.16048964, 0.04356923, 0.25165440],
           [0.16538900, 0.04504430, 0.25805096],
           [0.17028593, 0.04645678, 0.26449657],
           [0.17518003, 0.04780676, 0.27099345],
           [0.18007074, 0.04909437, 0.27754379],
           [0.18495762, 0.05031912, 0.28415040],
           [0.18984008, 0.05148049, 0.29081625],
           [0.19471647, 0.05258010, 0.29754239],
           [0.19958618, 0.05361678, 0.30433270],
           [0.20444751, 0.05459151, 0.31118919],
           [0.20929922, 0.05550376, 0.31811564],
           [0.21413882, 0.05635561, 0.32511367],
           [0.21896421, 0.05714769, 0.33218672],
           [0.22377274, 0.05788148, 0.33933794],
           [0.22856112, 0.05855955, 0.34657012],
           [0.23332527, 0.05918597, 0.35388549],
           [0.23806040, 0.05976622, 0.36128589],
           [0.24276170, 0.06030484, 0.36877533],
           [0.24742193, 0.06081291, 0.37635309],
           [0.25203344, 0.06130190, 0.38401992],
           [0.25658695, 0.06178750, 0.39177471],
           [0.26107122, 0.06229107, 0.39961346],
           [0.26547353, 0.06283783, 0.40753129],
           [0.26977818, 0.06346323, 0.41551642],
           [0.27396773, 0.06420866, 0.42355414],
           [0.27802236, 0.06512511, 0.43162229],
           [0.28192067, 0.06627120, 0.43969143],
           [0.28564067, 0.06771084, 0.44772416],
           [0.28916153, 0.06950790, 0.45567615],
           [0.29246553, 0.07171986, 0.46349748],
           [0.29554035, 0.07438845, 0.47113807],
           [0.29838062, 0.07753367, 0.47855166],
           [0.30098832, 0.08115027, 0.48570117],
           [0.30337211, 0.08520982, 0.49256135],
           [0.30554562, 0.08966644, 0.49911944],
           [0.30752549, 0.09446421, 0.50537395],
           [0.30932949, 0.09954425, 0.51133228],
           [0.31097525, 0.10484997, 0.51700784],
           [0.31247949, 0.11033024, 0.52241746],
           [0.31385726, 0.11594089, 0.52757996],
           [0.31512203, 0.12164498, 0.53251446],
           [0.31628568, 0.12741224, 0.53723953],
           [0.31735854, 0.13321839, 0.54177283],
           [0.31835001, 0.13904386, 0.54613054],
           [0.31926756, 0.14487382, 0.55032795],
           [0.32011852, 0.15069617, 0.55437862],
           [0.32090857, 0.15650214, 0.55829515],
           [0.32164315, 0.16228476, 0.56208877],
           [0.32232701, 0.16803883, 0.56576971],
           [0.32296429, 0.17376059, 0.56934720],
           [0.32355864, 0.17944737, 0.57282963],
           [0.32411325, 0.18509739, 0.57622458],
           [0.32463109, 0.19070950, 0.57953893],
           [0.32511520, 0.19628275, 0.58277894],
           [0.32556731, 0.20181740, 0.58595028],
           [0.32599029, 0.20731304, 0.58905819],
           [0.32638545, 0.21277047, 0.59210735],
           [0.32675517, 0.21818982, 0.59510216],
           [0.32710078, 0.22357199, 0.59804657],
           [0.32742372, 0.22891779, 0.60094423],
           [0.32772546, 0.23422805, 0.60379849],
           [0.32800753, 0.23950350, 0.60661251],
           [0.32827086, 0.24474529, 0.60938909],
           [0.32851655, 0.24995439, 0.61213087],
           [0.32874562, 0.25513180, 0.61484030],
           [0.32895901, 0.26027851, 0.61751963],
           [0.32915760, 0.26539554, 0.62017096],
           [0.32934219, 0.27048388, 0.62279622],
           [0.32951352, 0.27554451, 0.62539722],
           [0.32967230, 0.28057842, 0.62797564],
           [0.32981935, 0.28558646, 0.63053307],
           [0.32995511, 0.29056966, 0.63307091],
           [0.33008013, 0.29552896, 0.63559052],
           [0.33019492, 0.30046524, 0.63809313],
           [0.33030002, 0.30537937, 0.64057992],
           [0.33039611, 0.31027209, 0.64305205],
           [0.33048336, 0.31514436, 0.64551044],
           [0.33056217, 0.31999699, 0.64795602],
           [0.33063313, 0.32483066, 0.65038975],
           [0.33069649, 0.32964620, 0.65281239],
           [0.33075249, 0.33444438, 0.65522465],
           [0.33080168, 0.33922584, 0.65762731],
           [0.33084419, 0.34399134, 0.66002095],
           [0.33088029, 0.34874158, 0.66240616],
           [0.33091044, 0.35347713, 0.66478356],
           [0.33093467, 0.35819875, 0.66715355],
           [0.33095340, 0.36290697, 0.66951665],
           [0.33096677, 0.36760245, 0.67187325],
           [0.33097501, 0.37228577, 0.67422372],
           [0.33097842, 0.37695748, 0.67656841],
           [0.33097710, 0.38161819, 0.67890758],
           [0.33097139, 0.38626838, 0.68124155],
           [0.33096137, 0.39090862, 0.68357049],
           [0.33094738, 0.39553939, 0.68589463],
           [0.33092952, 0.40016122, 0.68821410],
           [0.33090807, 0.40477455, 0.69052904],
           [0.33088322, 0.40937987, 0.69283954],
           [0.33085521, 0.41397764, 0.69514566],
           [0.33082428, 0.41856828, 0.69744743],
           [0.33079066, 0.42315222, 0.69974485],
           [0.33075463, 0.42772987, 0.70203789],
           [0.33071647, 0.43230164, 0.70432650],
           [0.33067647, 0.43686790, 0.70661057],
           [0.33063497, 0.44142902, 0.70888999],
           [0.33059226, 0.44598538, 0.71116461],
           [0.33054882, 0.45053728, 0.71343427],
           [0.33050491, 0.45508511, 0.71569871],
           [0.33046115, 0.45962913, 0.71795776],
           [0.33041781, 0.46416971, 0.72021108],
           [0.33037561, 0.46870707, 0.72245843],
           [0.33033499, 0.47324154, 0.72469945],
           [0.33029663, 0.47777335, 0.72693378],
           [0.33026124, 0.48230276, 0.72916105],
           [0.33022942, 0.48683003, 0.73138079],
           [0.33020219, 0.49135531, 0.73359262],
           [0.33018021, 0.49587889, 0.73579597],
           [0.33016456, 0.50040091, 0.73799036],
           [0.33015640, 0.50492150, 0.74017529],
           [0.33015652, 0.50944094, 0.74235001],
           [0.33016648, 0.51395924, 0.74451405],
           [0.33018763, 0.51847654, 0.74666673],
           [0.33022112, 0.52299303, 0.74880723],
           [0.33026881, 0.52750870, 0.75093493],
           [0.33033245, 0.53202361, 0.75304905],
           [0.33041385, 0.53653780, 0.75514877],
           [0.33051483, 0.54105136, 0.75723312],
           [0.33063782, 0.54556419, 0.75930132],
           [0.33078520, 0.55007627, 0.76135243],
           [0.33095951, 0.55458753, 0.76338544],
           [0.33116353, 0.55909787, 0.76539934],
           [0.33140020, 0.56360719, 0.76739302],
           [0.33167268, 0.56811535, 0.76936532],
           [0.33198457, 0.57262211, 0.77131513],
           [0.33233962, 0.57712725, 0.77324124],
           [0.33274186, 0.58163048, 0.77514237],
           [0.33319562, 0.58613150, 0.77701722],
           [0.33370556, 0.59062994, 0.77886443],
           [0.33427662, 0.59512540, 0.78068255],
           [0.33491406, 0.59961743, 0.78247010],
           [0.33562372, 0.60410547, 0.78422564],
           [0.33641171, 0.60858894, 0.78594765],
           [0.33728457, 0.61306716, 0.78763459],
           [0.33824910, 0.61753946, 0.78928477],
           [0.33931249, 0.62200507, 0.79089643],
           [0.34048286, 0.62646302, 0.79246820],
           [0.34176815, 0.63091242, 0.79399821],
           [0.34317705, 0.63535220, 0.79548484],
           [0.34471872, 0.63978118, 0.79692655],
           [0.34640249, 0.64419817, 0.79832162],
           [0.34823828, 0.64860177, 0.79966860],
           [0.35023639, 0.65299050, 0.80096621],
           [0.35240696, 0.65736289, 0.80221273],
           [0.35476094, 0.66171715, 0.80340742],
           [0.35730905, 0.66605153, 0.80454930],
           [0.36006205, 0.67036412, 0.80563769],
           [0.36303051, 0.67465296, 0.80667226],
           [0.36622473, 0.67891598, 0.80765298],
           [0.36965449, 0.68315103, 0.80858050],
           [0.37332879, 0.68735594, 0.80945583],
           [0.37725565, 0.69152854, 0.81028057],
           [0.38144179, 0.69566668, 0.81105701],
           [0.38589243, 0.69976829, 0.81178814],
           [0.39061094, 0.70383141, 0.81247768],
           [0.39559867, 0.70785428, 0.81313008],
           [0.40085473, 0.71183537, 0.81375048],
           [0.40637584, 0.71577343, 0.81434474],
           [0.41215626, 0.71966756, 0.81491933],
           [0.41818783, 0.72351722, 0.81548120],
           [0.42446014, 0.72732228, 0.81603761],
           [0.43096069, 0.73108304, 0.81659606],
           [0.43767520, 0.73480020, 0.81716407],
           [0.44458799, 0.73847485, 0.81774903],
           [0.45168236, 0.74210845, 0.81835806],
           [0.45894105, 0.74570279, 0.81899783],
           [0.46634662, 0.74925990, 0.81967446],
           [0.47388188, 0.75278203, 0.82039341],
           [0.48153025, 0.75627154, 0.82115944],
           [0.48927559, 0.75973094, 0.82197684],
           [0.49710255, 0.76316282, 0.82284942],
           [0.50499805, 0.76656958, 0.82377935],
           [0.51294815, 0.76995391, 0.82476983],
           [0.52094213, 0.77331809, 0.82582191],
           [0.52896959, 0.77666450, 0.82693685],
           [0.53702081, 0.77999544, 0.82811581],
           [0.54508743, 0.78331310, 0.82935933],
           [0.55316270, 0.78661943, 0.83066727],
           [0.56124038, 0.78991633, 0.83203948],
           [0.56931446, 0.79320572, 0.83347602],
           [0.57738057, 0.79648922, 0.83497618],
           [0.58543520, 0.79976832, 0.83653902],
           [0.59347520, 0.80304444, 0.83816366],
           [0.60149600, 0.80631930, 0.83985030],
           [0.60949780, 0.80959366, 0.84159649],
           [0.61747594, 0.81286927, 0.84340291],
           [0.62543124, 0.81614675, 0.84526715],
           [0.63336132, 0.81942736, 0.84718888],
           [0.64126483, 0.82271216, 0.84916731],
           [0.64914193, 0.82600186, 0.85120091],
           [0.65699192, 0.82929734, 0.85328879],
           [0.66481429, 0.83259942, 0.85543006],
           [0.67260878, 0.83590887, 0.85762378],
           [0.68037529, 0.83922639, 0.85986905],
           [0.68811387, 0.84255265, 0.86216492],
           [0.69582471, 0.84588824, 0.86451049],
           [0.70350814, 0.84923374, 0.86690483],
           [0.71116455, 0.85258966, 0.86934706],
           [0.71879446, 0.85595650, 0.87183627],
           [0.72639742, 0.85933496, 0.87437213],
           [0.73397405, 0.86272548, 0.87695378],
           [0.74152578, 0.86612825, 0.87958001],
           [0.74905216, 0.86954396, 0.88225059],
           [0.75655360, 0.87297306, 0.88496491],
           [0.76403187, 0.87641559, 0.88772171],
           [0.77148527, 0.87987258, 0.89052147],
           [0.77891692, 0.88334365, 0.89336233],
           [0.78632472, 0.88682992, 0.89624501],
           [0.79371145, 0.89033111, 0.89916789],
           [0.80107621, 0.89384796, 0.90213114],
           [0.80841988, 0.89738070, 0.90513410],
           [0.81574379, 0.90092943, 0.90817593],
           [0.82304670, 0.90449497, 0.91125697],
           [0.83033023, 0.90807731, 0.91437629],
           [0.83759510, 0.91167669, 0.91753337],
           [0.84484145, 0.91529351, 0.92072797],
           [0.85206864, 0.91892841, 0.92396022],
           [0.85927824, 0.92258135, 0.92722925],
           [0.86647054, 0.92625267, 0.93053477],
           [0.87364582, 0.92994270, 0.93387654],
           [0.88080434, 0.93365179, 0.93725430],
           [0.88794635, 0.93738028, 0.94066779],
           [0.89507189, 0.94112856, 0.94411689],
           [0.90218116, 0.94489699, 0.94760135],
           [0.90927462, 0.94868582, 0.95112086],
           [0.91635237, 0.95249543, 0.95467523],
           [0.92341450, 0.95632620, 0.95826430],
           [0.93046101, 0.96017851, 0.96188789],
           [0.93749188, 0.96405279, 0.96554587],
           [0.94450698, 0.96794949, 0.96923810],
           [0.95150590, 0.97186913, 0.97296456],
           [0.95848829, 0.97581226, 0.97672516],
           [0.96545389, 0.97977938, 0.98051973],
           [0.97240208, 0.98377110, 0.98434820],
           [0.97933207, 0.98778813, 0.98821051],
           [0.98624277, 0.99183128, 0.99210660],
           [0.99313272, 0.99590152, 0.99603643],
           [1.00000000, 1.00000000, 1.00000000],
           [0.99651279, 0.99457267, 0.99605330],
           [0.99295334, 0.98919689, 0.99211967],
           [0.98932435, 0.98386929, 0.98822156],
           [0.98563710, 0.97858296, 0.98438205],
           [0.98190830, 0.97332938, 0.98061866],
           [0.97815979, 0.96809863, 0.97694203],
           [0.97441507, 0.96288076, 0.97335603],
           [0.97069299, 0.95766849, 0.96985624],
           [0.96700845, 0.95245638, 0.96643513],
           [0.96337244, 0.94724054, 0.96308497],
           [0.95978968, 0.94201980, 0.95979570],
           [0.95626344, 0.93679325, 0.95656031],
           [0.95279443, 0.93156093, 0.95337247],
           [0.94938114, 0.92632374, 0.95022607],
           [0.94602365, 0.92108154, 0.94711876],
           [0.94271865, 0.91583587, 0.94404559],
           [0.93946518, 0.91058689, 0.94100512],
           [0.93626095, 0.90533547, 0.93799495],
           [0.93310402, 0.90008221, 0.93501341],
           [0.92999326, 0.89482732, 0.93205984],
           [0.92692614, 0.88957170, 0.92913222],
           [0.92390249, 0.88431502, 0.92623104],
           [0.92091949, 0.87905837, 0.92335402],
           [0.91797763, 0.87380105, 0.92050229],
           [0.91507404, 0.86854419, 0.91767352],
           [0.91220953, 0.86328695, 0.91486902],
           [0.90938150, 0.85803032, 0.91208670],
           [0.90659062, 0.85277353, 0.90932766],
           [0.90383493, 0.84751726, 0.90659035],
           [0.90111453, 0.84226104, 0.90387522],
           [0.89842849, 0.83700500, 0.90118166],
           [0.89577587, 0.83174925, 0.89850906],
           [0.89315720, 0.82649314, 0.89585812],
           [0.89057044, 0.82123736, 0.89322714],
           [0.88801673, 0.81598094, 0.89061734],
           [0.88549454, 0.81072431, 0.88802744],
           [0.88300327, 0.80546743, 0.88545701],
           [0.88054402, 0.80020928, 0.88290716],
           [0.87811483, 0.79495059, 0.88037614],
           [0.87571567, 0.78969098, 0.87786399],
           [0.87334737, 0.78442958, 0.87537150],
           [0.87100825, 0.77916694, 0.87289716],
           [0.86869808, 0.77390280, 0.87044077],
           [0.86641783, 0.76863621, 0.86800316],
           [0.86416627, 0.76336745, 0.86558323],
           [0.86194295, 0.75809639, 0.86318050],
           [0.85974766, 0.75282271, 0.86079476],
           [0.85758121, 0.74754554, 0.85842661],
           [0.85544254, 0.74226507, 0.85607506],
           [0.85333129, 0.73698107, 0.85373967],
           [0.85124729, 0.73169321, 0.85142019],
           [0.84919036, 0.72640114, 0.84911633],
           [0.84716058, 0.72110440, 0.84682801],
           [0.84515800, 0.71580247, 0.84455512],
           [0.84318193, 0.71049530, 0.84229690],
           [0.84123219, 0.70518254, 0.84005301],
           [0.83930863, 0.69986380, 0.83782312],
           [0.83741109, 0.69453869, 0.83560689],
           [0.83553939, 0.68920682, 0.83340395],
           [0.83369338, 0.68386778, 0.83121390],
           [0.83187287, 0.67852116, 0.82903636],
           [0.83007770, 0.67316655, 0.82687091],
           [0.82830769, 0.66780353, 0.82471710],
           [0.82656264, 0.66243165, 0.82257448],
           [0.82484238, 0.65705050, 0.82044255],
           [0.82314670, 0.65165962, 0.81832083],
           [0.82147539, 0.64625857, 0.81620877],
           [0.81982831, 0.64084683, 0.81410588],
           [0.81820602, 0.63542346, 0.81201217],
           [0.81660754, 0.62998844, 0.80992647],
           [0.81503263, 0.62454131, 0.80784811],
           [0.81348102, 0.61908158, 0.80577642],
           [0.81195295, 0.61360845, 0.80371107],
           [0.81044872, 0.60812102, 0.80165175],
           [0.80896705, 0.60261944, 0.79959694],
           [0.80750784, 0.59710307, 0.79754597],
           [0.80607236, 0.59157031, 0.79549913],
           [0.80465854, 0.58602181, 0.79345426],
           [0.80326733, 0.58045616, 0.79141135],
           [0.80189818, 0.57487292, 0.78936925],
           [0.80055066, 0.56927159, 0.78732688],
           [0.79922505, 0.56365113, 0.78528362],
           [0.79792067, 0.55801115, 0.78323812],
           [0.79663727, 0.55235096, 0.78118929],
           [0.79537530, 0.54666931, 0.77913647],
           [0.79413326, 0.54096635, 0.77707762],
           [0.79291197, 0.53524054, 0.77501220],
           [0.79171097, 0.52949121, 0.77293875],
           [0.79052936, 0.52371801, 0.77085549],
           [0.78936697, 0.51792004, 0.76876103],
           [0.78822356, 0.51209640, 0.76665385],
           [0.78709931, 0.50624585, 0.76453263],
           [0.78599327, 0.50036798, 0.76239525],
           [0.78490498, 0.49446198, 0.76023983],
           [0.78383399, 0.48852703, 0.75806439],
           [0.78277976, 0.48256230, 0.75586683],
           [0.78174219, 0.47656663, 0.75364514],
           [0.78072052, 0.47053932, 0.75139686],
           [0.77971380, 0.46447985, 0.74911932],
           [0.77872116, 0.45838757, 0.74680980],
           [0.77774249, 0.45226120, 0.74446580],
           [0.77677689, 0.44610008, 0.74208428],
           [0.77582269, 0.43990422, 0.73966173],
           [0.77488027, 0.43367180, 0.73719540],
           [0.77394729, 0.42740341, 0.73468119],
           [0.77302307, 0.42109815, 0.73211556],
           [0.77210681, 0.41475523, 0.72949473],
           [0.77119639, 0.40837505, 0.72681422],
           [0.77029043, 0.40195737, 0.72406970],
           [0.76938735, 0.39550218, 0.72125655],
           [0.76848530, 0.38900973, 0.71836989],
           [0.76758217, 0.38248060, 0.71540459],
           [0.76667560, 0.37591567, 0.71235530],
           [0.76576298, 0.36931620, 0.70921645],
           [0.76484255, 0.36268265, 0.70598248],
           [0.76391008, 0.35601815, 0.70264727],
           [0.76296333, 0.34932397, 0.69920494],
           [0.76199799, 0.34260370, 0.69564932],
           [0.76101097, 0.33585991, 0.69197435],
           [0.75999801, 0.32909662, 0.68817393],
           [0.75895465, 0.32231841, 0.68424218],
           [0.75787635, 0.31553025, 0.68017342],
           [0.75675826, 0.30873782, 0.67596237],
           [0.75559539, 0.30194734, 0.67160418],
           [0.75438284, 0.29516537, 0.66709455],
           [0.75311490, 0.28839979, 0.66243012],
           [0.75178649, 0.28165822, 0.65760819],
           [0.75039239, 0.27494887, 0.65262711],
           [0.74892756, 0.26828019, 0.64748627],
           [0.74738705, 0.26166089, 0.64218628],
           [0.74576659, 0.25509928, 0.63672872],
           [0.74406206, 0.24860376, 0.63111651],
           [0.74226991, 0.24218234, 0.62535367],
           [0.74038720, 0.23584244, 0.61944523],
           [0.73841159, 0.22959089, 0.61339718],
           [0.73634138, 0.22343379, 0.60721632],
           [0.73417548, 0.21737647, 0.60091011],
           [0.73191343, 0.21142341, 0.59448655],
           [0.72955534, 0.20557825, 0.58795396],
           [0.72710185, 0.19984378, 0.58132089],
           [0.72455408, 0.19422203, 0.57459594],
           [0.72191353, 0.18871428, 0.56778764],
           [0.71918207, 0.18332113, 0.56090439],
           [0.71636182, 0.17804261, 0.55395435],
           [0.71345514, 0.17287823, 0.54694533],
           [0.71046452, 0.16782704, 0.53988482],
           [0.70739256, 0.16288778, 0.53277991],
           [0.70424194, 0.15805887, 0.52563728],
           [0.70101532, 0.15333854, 0.51846324],
           [0.69771539, 0.14872485, 0.51126365],
           [0.69434476, 0.14421578, 0.50404407],
           [0.69090599, 0.13980924, 0.49680957],
           [0.68740160, 0.13550312, 0.48956488],
           [0.68383396, 0.13129538, 0.48231439],
           [0.68020538, 0.12718398, 0.47506230],
           [0.67651804, 0.12316702, 0.46781232],
           [0.67277403, 0.11924270, 0.46056795],
           [0.66897531, 0.11540930, 0.45333258],
           [0.66512374, 0.11166532, 0.44610916],
           [0.66122104, 0.10800938, 0.43890055],
           [0.65726885, 0.10444028, 0.43170947],
           [0.65326868, 0.10095703, 0.42453832],
           [0.64922193, 0.09755882, 0.41738951],
           [0.64512991, 0.09424507, 0.41026521],
           [0.64099380, 0.09101541, 0.40316752],
           [0.63681472, 0.08786969, 0.39609844],
           [0.63259366, 0.08480802, 0.38905987],
           [0.62833154, 0.08183073, 0.38205363],
           [0.62402916, 0.07893840, 0.37508149],
           [0.61968727, 0.07613188, 0.36814517],
           [0.61530651, 0.07341226, 0.36124635],
           [0.61088745, 0.07078087, 0.35438670],
           [0.60643058, 0.06823934, 0.34756782],
           [0.60193631, 0.06578946, 0.34079141],
           [0.59740499, 0.06343336, 0.33405903],
           [0.59283687, 0.06117329, 0.32737240],
           [0.58823217, 0.05901171, 0.32073323],
           [0.58359100, 0.05695140, 0.31414312],
           [0.57891345, 0.05499505, 0.30760396],
           [0.57419952, 0.05314552, 0.30111757],
           [0.56944915, 0.05140588, 0.29468575],
           [0.56466224, 0.04977894, 0.28831055],
           [0.55983864, 0.04826751, 0.28199404],
           [0.55497814, 0.04687425, 0.27573840],
           [0.55008047, 0.04560157, 0.26954588],
           [0.54514535, 0.04445164, 0.26341884],
           [0.54017244, 0.04342599, 0.25735987],
           [0.53516140, 0.04252573, 0.25137164],
           [0.53011186, 0.04175134, 0.24545699],
           [0.52502344, 0.04110259, 0.23961888],
           [0.51989576, 0.04057848, 0.23386046],
           [0.51472846, 0.04017305, 0.22818504],
           [0.50952123, 0.03988862, 0.22259608],
           [0.50427376, 0.03972237, 0.21709714],
           [0.49898586, 0.03966871, 0.21169200],
           [0.49365742, 0.03972170, 0.20638454],
           [0.48828845, 0.03987500, 0.20117868],
           [0.48287908, 0.04012181, 0.19607839],
           [0.47742962, 0.04045479, 0.19108759],
           [0.47194057, 0.04085798, 0.18621023],
           [0.46641267, 0.04132655, 0.18145004],
           [0.46084684, 0.04185049, 0.17681050],
           [0.45524431, 0.04241927, 0.17229482],
           [0.44960653, 0.04302226, 0.16790577],
           [0.44393524, 0.04364857, 0.16364563],
           [0.43823240, 0.04428757, 0.15951608],
           [0.43250021, 0.04492881, 0.15551812],
           [0.42674110, 0.04556211, 0.15165204],
           [0.42095767, 0.04617782, 0.14791737],
           [0.41515258, 0.04676711, 0.14431283],
           [0.40932862, 0.04732177, 0.14083637],
           [0.40348860, 0.04783442, 0.13748522],
           [0.39763529, 0.04829855, 0.13425593],
           [0.39177139, 0.04870857, 0.13114443],
           [0.38589948, 0.04905982, 0.12814615],
           [0.38002216, 0.04934797, 0.12525607],
           [0.37414156, 0.04957039, 0.12246885],
           [0.36825982, 0.04972466, 0.11977893],
           [0.36237886, 0.04980896, 0.11718058],
           [0.35650045, 0.04982209, 0.11466802],
           [0.35062596, 0.04976376, 0.11223548],
           [0.34475674, 0.04963364, 0.10987725],
           [0.33889396, 0.04943184, 0.10758771],
           [0.33303856, 0.04915884, 0.10536139],
           [0.32719128, 0.04881541, 0.10319302],
           [0.32135268, 0.04840259, 0.10107755],
           [0.31552330, 0.04792126, 0.09901007],
           [0.30970366, 0.04737220, 0.09698582],
           [0.30389366, 0.04675731, 0.09500056],
           [0.29809379, 0.04607701, 0.09304982],
           [0.29230391, 0.04533292, 0.09112969],
           [0.28652391, 0.04452634, 0.08923639],
           [0.28075373, 0.04365829, 0.08736623],
           [0.27499325, 0.04272978, 0.08551573],
           [0.26924223, 0.04174182, 0.08368156],
           [0.26350036, 0.04069541, 0.08186061],
           [0.25776724, 0.03958238, 0.08004990],
           [0.25204242, 0.03842694, 0.07824664],
           [0.24632534, 0.03723743, 0.07644816],
           [0.24061554, 0.03601731, 0.07465184],
           [0.23491278, 0.03476951, 0.07285486],
           [0.22921589, 0.03349840, 0.07105533],
           [0.22352481, 0.03220647, 0.06925037],
           [0.21783824, 0.03089799, 0.06743829],
           [0.21215613, 0.02957523, 0.06561621],
           [0.20647710, 0.02824235, 0.06378257],
           [0.20080045, 0.02690234, 0.06193512],
           [0.19512565, 0.02555789, 0.06007140],
           [0.18945137, 0.02421263, 0.05818973],
           [0.18377664, 0.02286958, 0.05628802],
           [0.17810042, 0.02153175, 0.05436418],
           [0.17242157, 0.02020212, 0.05241613],
           [0.16673885, 0.01888366, 0.05044177],
           [0.16105095, 0.01757931, 0.04843897],
           [0.15535642, 0.01629201, 0.04640560]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.viola', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
