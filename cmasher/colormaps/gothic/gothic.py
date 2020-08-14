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
cm_type = 'sequential'

# RGB-values of this colormap
cm_data = [[0.00000000, 0.00000000, 0.00000000],
           [0.00022645, 0.00022909, 0.00031205],
           [0.00077823, 0.00079287, 0.00113479],
           [0.00159943, 0.00163923, 0.00245504],
           [0.00266447, 0.00274448, 0.00428572],
           [0.00395711, 0.00409318, 0.00664640],
           [0.00546582, 0.00567389, 0.00956002],
           [0.00718195, 0.00747748, 0.01305173],
           [0.00909884, 0.00949624, 0.01714836],
           [0.01121123, 0.01172343, 0.02187862],
           [0.01351491, 0.01415290, 0.02727369],
           [0.01600681, 0.01677913, 0.03336359],
           [0.01868456, 0.01959684, 0.04018079],
           [0.02154643, 0.02260097, 0.04728996],
           [0.02459131, 0.02578663, 0.05441304],
           [0.02781831, 0.02914861, 0.06156474],
           [0.03122766, 0.03268232, 0.06874791],
           [0.03481989, 0.03638295, 0.07596749],
           [0.03859596, 0.04024559, 0.08322812],
           [0.04249080, 0.04410219, 0.09053889],
           [0.04634300, 0.04789090, 0.09789982],
           [0.05016328, 0.05161717, 0.10531366],
           [0.05395562, 0.05528234, 0.11278715],
           [0.05772405, 0.05888786, 0.12032344],
           [0.06147258, 0.06243542, 0.12792196],
           [0.06520452, 0.06592517, 0.13559036],
           [0.06892348, 0.06935798, 0.14332966],
           [0.07263293, 0.07273481, 0.15113921],
           [0.07633583, 0.07605431, 0.15903040],
           [0.08003570, 0.07931811, 0.16699615],
           [0.08373552, 0.08252464, 0.17504637],
           [0.08743849, 0.08567440, 0.18317848],
           [0.09114768, 0.08876606, 0.19139854],
           [0.09486620, 0.09179938, 0.19970608],
           [0.09859718, 0.09477271, 0.20810670],
           [0.10234364, 0.09768588, 0.21659803],
           [0.10610892, 0.10053595, 0.22518950],
           [0.10989591, 0.10332336, 0.23387469],
           [0.11370815, 0.10604441, 0.24266431],
           [0.11754870, 0.10869837, 0.25155543],
           [0.12142072, 0.11128363, 0.26054831],
           [0.12532812, 0.11379583, 0.26965290],
           [0.12927396, 0.11623390, 0.27886548],
           [0.13326166, 0.11859530, 0.28818729],
           [0.13729483, 0.12087686, 0.29762085],
           [0.14137770, 0.12307381, 0.30717314],
           [0.14551365, 0.12518370, 0.31684199],
           [0.14970647, 0.12720285, 0.32662861],
           [0.15396012, 0.12912700, 0.33653492],
           [0.15827870, 0.13095158, 0.34656263],
           [0.16266636, 0.13267169, 0.35671319],
           [0.16712736, 0.13428210, 0.36698775],
           [0.17166604, 0.13577720, 0.37738708],
           [0.17628676, 0.13715106, 0.38791153],
           [0.18099397, 0.13839736, 0.39856098],
           [0.18579234, 0.13950895, 0.40933577],
           [0.19068775, 0.14047608, 0.42024045],
           [0.19568351, 0.14129342, 0.43126754],
           [0.20078404, 0.14195304, 0.44241416],
           [0.20599668, 0.14244100, 0.45368768],
           [0.21132371, 0.14275208, 0.46507517],
           [0.21677202, 0.14287187, 0.47658004],
           [0.22234439, 0.14279263, 0.48819038],
           [0.22804878, 0.14249613, 0.49991061],
           [0.23388712, 0.14197420, 0.51172456],
           [0.23986439, 0.14121182, 0.52362522],
           [0.24598522, 0.14019328, 0.53560330],
           [0.25225367, 0.13890228, 0.54764686],
           [0.25867314, 0.13732217, 0.55974103],
           [0.26524609, 0.13543610, 0.57186764],
           [0.27197387, 0.13322737, 0.58400499],
           [0.27885652, 0.13067976, 0.59612760],
           [0.28589459, 0.12777350, 0.60821056],
           [0.29308561, 0.12449255, 0.62022159],
           [0.30042558, 0.12082165, 0.63212506],
           [0.30790750, 0.11674965, 0.64387981],
           [0.31552419, 0.11226371, 0.65544484],
           [0.32326472, 0.10735770, 0.66677344],
           [0.33111488, 0.10203244, 0.67781540],
           [0.33905913, 0.09629226, 0.68852123],
           [0.34707951, 0.09014907, 0.69884138],
           [0.35515527, 0.08362585, 0.70872716],
           [0.36326513, 0.07675309, 0.71813500],
           [0.37138881, 0.06956632, 0.72702887],
           [0.37950397, 0.06211954, 0.73537751],
           [0.38759174, 0.05447100, 0.74316081],
           [0.39563394, 0.04669732, 0.75036671],
           [0.40361591, 0.03888062, 0.75699326],
           [0.41152530, 0.03164047, 0.76304669],
           [0.41935304, 0.02543815, 0.76854103],
           [0.42709298, 0.02031114, 0.77349649],
           [0.43474152, 0.01627626, 0.77793798],
           [0.44229742, 0.01333169, 0.78189376],
           [0.44976135, 0.01146067, 0.78539411],
           [0.45713549, 0.01063463, 0.78847022],
           [0.46442309, 0.01081659, 0.79115334],
           [0.47162855, 0.01196218, 0.79347397],
           [0.47875608, 0.01402579, 0.79546171],
           [0.48581114, 0.01695648, 0.79714435],
           [0.49279879, 0.02070472, 0.79854816],
           [0.49972391, 0.02522195, 0.79969780],
           [0.50659185, 0.03045917, 0.80061571],
           [0.51340745, 0.03637043, 0.80132269],
           [0.52017534, 0.04282908, 0.80183785],
           [0.52689980, 0.04930069, 0.80217867],
           [0.53358513, 0.05569514, 0.80236078],
           [0.54023517, 0.06199196, 0.80239848],
           [0.54685349, 0.06817923, 0.80230470],
           [0.55344338, 0.07425066, 0.80209106],
           [0.56000786, 0.08020382, 0.80176804],
           [0.56654970, 0.08603884, 0.80134499],
           [0.57307144, 0.09175756, 0.80083024],
           [0.57957534, 0.09736306, 0.80023124],
           [0.58606346, 0.10285920, 0.79955460],
           [0.59253760, 0.10825041, 0.79880617],
           [0.59899939, 0.11354145, 0.79799109],
           [0.60545023, 0.11873731, 0.79711382],
           [0.61189142, 0.12384306, 0.79617807],
           [0.61832389, 0.12886401, 0.79518730],
           [0.62474847, 0.13380547, 0.79414436],
           [0.63116578, 0.13867277, 0.79305161],
           [0.63757637, 0.14347123, 0.79191069],
           [0.64398050, 0.14820627, 0.79072306],
           [0.65037808, 0.15288348, 0.78949013],
           [0.65676913, 0.15750829, 0.78821218],
           [0.66315328, 0.16208639, 0.78688957],
           [0.66952977, 0.16662364, 0.78552262],
           [0.67589805, 0.17112589, 0.78411026],
           [0.68225674, 0.17559944, 0.78265234],
           [0.68860442, 0.18005080, 0.78114781],
           [0.69493963, 0.18448665, 0.77959431],
           [0.70125989, 0.18891443, 0.77799090],
           [0.70756261, 0.19334192, 0.77633520],
           [0.71384466, 0.19777760, 0.77462450],
           [0.72010221, 0.20223079, 0.77285577],
           [0.72633060, 0.20671182, 0.77102571],
           [0.73252455, 0.21123218, 0.76912938],
           [0.73867713, 0.21580506, 0.76716290],
           [0.74478041, 0.22044550, 0.76512015],
           [0.75082424, 0.22517106, 0.76299560],
           [0.75679634, 0.23000245, 0.76078196],
           [0.76268107, 0.23496446, 0.75847183],
           [0.76845920, 0.24008748, 0.75605407],
           [0.77410487, 0.24540882, 0.75352069],
           [0.77958481, 0.25097577, 0.75086016],
           [0.78485417, 0.25684877, 0.74806234],
           [0.78985171, 0.26310644, 0.74511919],
           [0.79449232, 0.26985063, 0.74203320],
           [0.79865801, 0.27721159, 0.73882784],
           [0.80219124, 0.28533969, 0.73558163],
           [0.80491044, 0.29436104, 0.73248071],
           [0.80668515, 0.30426502, 0.72986371],
           [0.80755994, 0.31479301, 0.72813763],
           [0.80777018, 0.32553117, 0.72754055],
           [0.80759002, 0.33614784, 0.72803657],
           [0.80721406, 0.34648292, 0.72944087],
           [0.80675023, 0.35649450, 0.73155302],
           [0.80625293, 0.36619295, 0.73420873],
           [0.80574916, 0.37560551, 0.73728435],
           [0.80525124, 0.38476330, 0.74068836],
           [0.80476631, 0.39369372, 0.74435284],
           [0.80429556, 0.40242328, 0.74822624],
           [0.80384088, 0.41097264, 0.75226912],
           [0.80340100, 0.41936153, 0.75645053],
           [0.80297646, 0.42760499, 0.76074589],
           [0.80256676, 0.43571672, 0.76513531],
           [0.80217086, 0.44370899, 0.76960252],
           [0.80178782, 0.45159243, 0.77413406],
           [0.80141847, 0.45937508, 0.77871854],
           [0.80106159, 0.46706561, 0.78334639],
           [0.80071701, 0.47467101, 0.78800940],
           [0.80038475, 0.48219746, 0.79270043],
           [0.80006474, 0.48965058, 0.79741327],
           [0.79975690, 0.49703552, 0.80214248],
           [0.79946120, 0.50435697, 0.80688321],
           [0.79917795, 0.51161899, 0.81163108],
           [0.79890750, 0.51882530, 0.81638215],
           [0.79864938, 0.52597991, 0.82113287],
           [0.79840452, 0.53308562, 0.82587986],
           [0.79817258, 0.54014587, 0.83062005],
           [0.79795429, 0.54716322, 0.83535046],
           [0.79774940, 0.55414065, 0.84006831],
           [0.79755887, 0.56108029, 0.84477081],
           [0.79738239, 0.56798489, 0.84945531],
           [0.79722053, 0.57485657, 0.85411909],
           [0.79707368, 0.58169742, 0.85875942],
           [0.79694199, 0.58850965, 0.86337353],
           [0.79682589, 0.59529518, 0.86795852],
           [0.79672587, 0.60205586, 0.87251137],
           [0.79664222, 0.60879360, 0.87702887],
           [0.79657547, 0.61551015, 0.88150762],
           [0.79652616, 0.62220720, 0.88594395],
           [0.79649489, 0.62888641, 0.89033393],
           [0.79648247, 0.63554933, 0.89467328],
           [0.79648976, 0.64219747, 0.89895736],
           [0.79651770, 0.64883234, 0.90318110],
           [0.79656775, 0.65545517, 0.90733900],
           [0.79664146, 0.66206725, 0.91142503],
           [0.79674047, 0.66866981, 0.91543262],
           [0.79686744, 0.67526370, 0.91935468],
           [0.79702485, 0.68184988, 0.92318342],
           [0.79721622, 0.68842894, 0.92691050],
           [0.79744560, 0.69500128, 0.93052694],
           [0.79771773, 0.70156710, 0.93402313],
           [0.79803853, 0.70812614, 0.93738897],
           [0.79841481, 0.71467785, 0.94061386],
           [0.79885450, 0.72122125, 0.94368690],
           [0.79936723, 0.72775467, 0.94659724],
           [0.79996338, 0.73427618, 0.94933404],
           [0.80065535, 0.74078294, 0.95188730],
           [0.80145671, 0.74727158, 0.95424806],
           [0.80238212, 0.75373814, 0.95640894],
           [0.80344734, 0.76017800, 0.95836491],
           [0.80466861, 0.76658610, 0.96011374],
           [0.80606200, 0.77295711, 0.96165649],
           [0.80764314, 0.77928548, 0.96299819],
           [0.80942583, 0.78556601, 0.96414739],
           [0.81142158, 0.79179405, 0.96511607],
           [0.81364007, 0.79796513, 0.96592084],
           [0.81608627, 0.80407665, 0.96657842],
           [0.81876351, 0.81012604, 0.96711014],
           [0.82167069, 0.81611261, 0.96753592],
           [0.82480425, 0.82203649, 0.96787645],
           [0.82815827, 0.82789867, 0.96815212],
           [0.83172483, 0.83370100, 0.96838198],
           [0.83549447, 0.83944605, 0.96858320],
           [0.83945680, 0.84513695, 0.96877075],
           [0.84360150, 0.85077649, 0.96896149],
           [0.84791706, 0.85636883, 0.96916391],
           [0.85239308, 0.86191695, 0.96939241],
           [0.85701875, 0.86742492, 0.96965302],
           [0.86178411, 0.87289609, 0.96995458],
           [0.86667964, 0.87833378, 0.97030452],
           [0.87169633, 0.88374121, 0.97070895],
           [0.87682575, 0.88912152, 0.97117283],
           [0.88206011, 0.89447768, 0.97170006],
           [0.88739220, 0.89981252, 0.97229365],
           [0.89281548, 0.90512870, 0.97295590],
           [0.89832334, 0.91042834, 0.97369376],
           [0.90391048, 0.91571404, 0.97450574],
           [0.90957132, 0.92098778, 0.97539652],
           [0.91530125, 0.92625168, 0.97636633],
           [0.92109508, 0.93150743, 0.97742103],
           [0.92694917, 0.93675703, 0.97855868],
           [0.93285924, 0.94200209, 0.97978284],
           [0.93882060, 0.94724412, 0.98109943],
           [0.94482994, 0.95248486, 0.98250786],
           [0.95088307, 0.95772588, 0.98401172],
           [0.95697549, 0.96296888, 0.98561499],
           [0.96310201, 0.96821576, 0.98732216],
           [0.96925629, 0.97346886, 0.98913827],
           [0.97543003, 0.97873120, 0.99106889],
           [0.98161171, 0.98400712, 0.99311960],
           [0.98778474, 0.98930311, 0.99529456],
           [0.99392516, 0.99462909, 0.99759278],
           [1.00000000, 1.00000000, 1.00000000]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.gothic', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
