from ctgan import CTGANSynthesizer
from pandas_profiling import ProfileReport
from utils import block, debug


with block('LOAD CTGAN'):
    pkl = './hotel_bookings.gan.pkl'
    gan = CTGANSynthesizer.load(pkl)
    print(gan.__dict__)


with block('GENERATE SYNTHETIC DATA'):
    synthetic_data = gan.sample(10000)
    print(synthetic_data)


with block('SAVE TO CSV'):
    target_location = "tmp/bookings.all.csv"
    print(target_location)
    synthetic_data.to_csv(
        target_location, 
        index=False
    )


with block('GENERATE PROFILE REPORT'):
    profile = ProfileReport(synthetic_data)
    target_location = "tmp/profile-report.html"
    profile.to_file(target_location)