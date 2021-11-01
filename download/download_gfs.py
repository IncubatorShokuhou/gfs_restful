from datetime import datetime, timedelta
import os


def download_gfs(download_time: datetime, ifore: int, resolution: int, main_dir: str):
    """Download the GFS file for the given download time .

    Args:
        download_time ([datetime]): [gfs数据的开始时间]
        ifore (int): [gfs数据的预报时次]
        resolution(int): [gfs数据的分辨率;25或50]
        main_dir (str): [gfs保存的主目录]
    """
    if download_time.hour % 6 != 0:
        raise ValueError("download_time must be on 0,6,12 or 18 o'clock")
    ifore_list = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        123,
        126,
        129,
        132,
        135,
        138,
        141,
        144,
        147,
        150,
        153,
        156,
        159,
        162,
        165,
        168,
        171,
        174,
        177,
        180,
        183,
        186,
        189,
        192,
        195,
        198,
        201,
        204,
        207,
        210,
        213,
        216,
        219,
        222,
        225,
        228,
        231,
        234,
        237,
        240,
        243,
        246,
        249,
        252,
        255,
        258,
        261,
        264,
        267,
        270,
        273,
        276,
        279,
        282,
        285,
        288,
        291,
        294,
        297,
        300,
        303,
        306,
        309,
        312,
        315,
        318,
        321,
        324,
        327,
        330,
        333,
        336,
        339,
        342,
        345,
        348,
        351,
        354,
        357,
        360,
        363,
        366,
        369,
        372,
        375,
        378,
        381,
        384,
    ]
    if resolution not in [25, 50]:
        raise ValueError("resolution must be 25 or 50")
    if ifore not in ifore_list:
        raise ValueError("ifore must be in %s" % ifore_list)
    else:
        url = download_time.strftime(
            f"https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.%Y%m%d/%H/atmos/gfs.t%Hz.pgrb2.0p{resolution}.f{str(ifore).zfill(3)}"
        )
        download_dir = os.path.join(
            main_dir,
            str(resolution),
            download_time.strftime("%Y"),
            download_time.strftime("%m"),
            download_time.strftime("%d"),
            download_time.strftime("%H"),
        )
        full_path = os.path.join(
            main_dir,
            str(resolution),
            download_time.strftime("%Y"),
            download_time.strftime("%m"),
            download_time.strftime("%d"),
            download_time.strftime("%H"),
            f"gfs.t%Hz.pgrb2.0p{resolution}.f{str(ifore).zfill(3)}",
        )
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
            
        if not os.path.exists(full_path):
            os.system(f"axel -n 32 -a {url} -o {download_dir}")
        else:
            if resolution == 50:
                if os.path.getsize(full_path) < 130*1024*1024: os.system(f"axel -n 32 -a {url} -o {download_dir}")
            else:
                if os.path.getsize(full_path) < 500*1024*1024: os.system(f"axel -n 32 -a {url} -o {download_dir}")
        return