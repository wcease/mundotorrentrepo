import xbmc
import os
from random import randint

def chaves():
    
    addonID = "plugin.video.mundotorrent"
    addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addonID)

    if not os.path.exists(addon_data_dir):
            os.makedirs(addon_data_dir)

    m3u =  os.path.join(addon_data_dir, "files.m3u")

    file = open(""+m3u+"","w")
    file.close


    eps = randint(1,170)
    ieps = 170 - eps

    eng2sp = {1:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/19302ca6.mp4",
    2:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/fd63d6a3.mp4",
    3:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/4efbbddc.mp4",                            
    4:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/385bae20.mp4",
    5:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/95e7a1e7.mp4",
    6:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/468978c5.mp4",
    7:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a56f0d96.mp4",
    8:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3f727aa7.mp4",
    9:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/23e730b5.mp4",
    10:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0f500990.mp4",
    11:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/98ceaf00.mp4",
    12:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/c3f335cc.mp4",
    13:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b8e84ed6.mp4",
    14:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a38cd93a.mp4",
    15:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/6412cd6d.mp4",
    16:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/abb59149.mp4",
    17:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1f08eb61.mp4",
    18:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/7eef4b16.mp4",
    19:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1699e490.mp4",
    20:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/14bda406.mp4",
    21:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/72e293ba.mp4",
    22:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2d6f88f3.mp4",
    23:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/8544a079.mp4",
    24:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/5152a234.mp4",
    25:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/fa8c76cc.mp4",
    26:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b0a02715.mp4",
    27:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/850ef314.mp4",
    28:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d09de6f6.mp4",
    29:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a56311d9.mp4",
    30:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/76ac45c0.mp4",
    31:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/9a96118e.mp4",
    32:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3b2374c1.mp4",
    33:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/808c0163.mp4",
    34:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/17f360dd.mp4",
    35:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/cc826836.mp4",
    36:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/64749e66.mp4",
    37:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/9854af7a.mp4",
    38:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/da546d5c.mp4",
    39:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/6642ce7d.mp4",
    40:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3e2722f7.mp4",
    41:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b68186ae.mp4",
    42:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0b58dbe7.mp4",
    43:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/26afb3ce.mp4",
    44:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/ee23b315.mp4",
    45:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d0fba958.mp4",
    46:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/453ab3d6.mp4",
    47:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/495a46cd.mp4",
    48:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b0e2df45.mp4",
    49:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d4ad7838.mp4",
    50:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1ce618b4.mp4",
    51:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3ed85ee2.mp4",
    52:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/6d73cb17.mp4",
    53:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2cb8f2cf.mp4",
    54:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/5e4971fe.mp4",
    55:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3cefff35.mp4",
    56:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/90a98a72.mp4",
    57:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/8dd3b7ba.mp4",
    58:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/8820ee38.mp4",
    59:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/bd280f31.mp4",
    60:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/33efc051.mp4",
    61:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b90c45b0.mp4",
    62:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/52e9e0e3.mp4",
    63:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0908825a.mp4",
    64:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/8ff1b195.mp4",
    65:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/54ae6a0c.mp4",
    66:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/983bc014.mp4",
    67:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/60154eb3.mp4",
    68:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1ba68fce.mp4",
    69:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/256e8cb7.mp4",
    70:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/ea02ebb6.mp4",
    71:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0e802e03.mp4",
    72:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/22e7f2cf.mp4",
    73:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/56cd67c8.mp4",
    74:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/cc5c7c61.mp4",
    75:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b5c9ced0.mp4",
    76:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/9a4e0146.mp4",
    77:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/566d6fcf.mp4",
    78:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/5200f700.mp4",
    79:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/75153908.mp4",
    80:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a65d243e.mp4",
    81:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2ad8e80b.mp4",
    82:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/7e9c0021.mp4",
    83:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/5b9d59ce.mp4",
    84:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2bfb3126.mp4",
    85:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/62975a34.mp4",
    86:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0fb9a2f3.mp4",
    87:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/92e851c6.mp4",
    88:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/4178bc37.mp4",
    89:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/ba4686f9.mp4",
    90:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2e5702c2.mp4",
    91:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/726db9f2.mp4",
    92:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d12de135.mp4",
    93:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b842991a.mp4",
    94:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0e63e384.mp4",
    95:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/ccba9742.mp4",
    96:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/309398ba.mp4",
    97:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/4d2a52ad.mp4",
    98:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/f9759dff.mp4",
    99:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/ebe696c3.mp4",
    100:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/dc561706.mp4",
    101:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d7828de2.mp4",
    102:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b1f7b5ae.mp4",
    103:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/452badda.mp4",
    104:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/53311bee.mp4",
    105:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b1f7b5ae.mp4",
    106:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3867b694.mp4",
    107:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/30a0d926.mp4",
    108:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/01a9b0ce.mp4",
    109:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/413c9ed6.mp4",
    110:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1cce2d4d.mp4",
    111:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/57a61f99.mp4",
    112:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/420f22af.mp4",
    113:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/475deb16.mp4",
    114:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a8126c11.mp4",
    115:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/f1eb1170.mp4",
    116:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/bb354e7d.mp4",
    117:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2fd7c153.mp4",
    118:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1ceee9d2.mp4",
    119:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3da3529c.mp4",
    120:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a5799a37.mp4",
    121:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b67ab490.mp4",
    122:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a05d3d80.mp4",
    123:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/af04c956.mp4",
    124:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/af1c2783.mp4",
    125:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/c351e732.mp4",
    126:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a5b3d8e6.mp4",
    127:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/c0901170.mp4",
    128:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/0ec14f1c.mp4",
    129:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/f52fb5b5.mp4",
    130:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/42ee0387.mp4",
    131:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/76d0d92c.mp4",
    132:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/fa357d10.mp4",
    133:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a1db2c27.mp4",
    134:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d8e1f094.mp4",
    135:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/9e72a823.mp4",
    136:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/c75d5bd7.mp4",
    137:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/dd30eed0.mp4",
    138:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d48b5929.mp4",
    139:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/2eea57eb.mp4",
    140:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/52ee7471.mp4",
    141:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/3516535a.mp4",
    142:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/e02eeb6e.mp4",
    143:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/130e4742.mp4",
    144:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/fefa3ed5.mp4",
    145:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a16824c9.mp4",
    146:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b7e8891d.mp4",
    147:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a58f8c9e.mp4",
    148:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/76ffb021.mp4",
    149:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b05a00ee.mp4",
    150:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/06d8464c.mp4",
    151:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/9a4307fc.mp4",
    152:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/7db6e3ec.mp4",
    153:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/61efe8b4.mp4",
    154:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/fbc65ca5.mp4",
    155:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/683e7d62.mp4",
    156:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/d36aa766.mp4",
    157:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/b1366d48.mp4",
    158:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/27edf991.mp4",
    159:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/f83aa3f9.mp4",
    160:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/965f721f.mp4",
    161:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/1d392059.mp4",
    162:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/8bc03f51.mp4",
    163:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/966a26f9.mp4",
    164:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/8cbc9c05.mp4",
    165:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/bfff7b26.mp4",
    166:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/a0da6ca7.mp4",
    167:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/fceb5c1e.mp4",
    168:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/7270a1b4.mp4",
    169:"http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer01/videos/f11f72e6.mp4",
    }

            
    for j in range(ieps,(ieps+30)):
            
            file = open(""+m3u+"","a")
            file.write(eng2sp[j])
            file.write("\n")
            file.close

            
    xbmc.Player().play(""+m3u+"")

