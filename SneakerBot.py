import requests
import random
import webbrowser
import bs4
import mechanicalsoup



# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/39.0.2171.95 Safari/537.36'}
class SneakerBot:
    def URLGen(model,size):
        BaseSize=580
        Shoesize = (float(size) - 6.5) * 20
        RawSize = Shoesize
        ShoeSizeCode = int(float(RawSize) + 580)
        URL = 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
        return URL;

    def CheckSizes(URL,model):
        print('checking sizes...')
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit/537.36 (KHTML,like Gecko)Chrome/39.0.2171.95 Safari/537.36'}
        RawHTML = requests.get(URL, headers=headers)
        Page = bs4.BeautifulSoup(RawHTML.text, "lxml")
        ListofRawSizes = Page.select('.size-dropdown-block')
        Sizes = str(ListofRawSizes[0].getText()).replace('\t','')
        Sizes = Sizes.replace('\n\n','')
        Sizes = Sizes.split()
        Sizes.remove('Select')
        Sizes.remove('size')
        print(Sizes)
        for size in Sizes:
            print(str(model) + ' Size ' + str(size) + ' Available ')

    def AddToCart(URL,self):

        browser = mechanicalsoup.StatefulBrowser
        browser.open("https://www.adidas.com/us/deerupt-runner-parley-shoes/CQ2623.html?forceSelSize=CQ2623_660")
        browser.launch_browser(self)



    # Model = input('model #')
    # Size = input('Size:  ')
    #  URL = URLGen(Model,float(Size))
    # CheckSizes(URL,Model)

    URL = ('https://www.adidas.com/us/deerupt-runner-parley-shoes/CQ2623.html?forceSelSize=CQ2623_660')
    AddToCart(URL, self)





