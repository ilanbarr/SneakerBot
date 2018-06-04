import requests
import random
import webbrowser
import bs4



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

    Model = input('model #')
    Size = input('Size:  ')
    URL = URLGen(Model,float(Size))
    print(str(URL))

    def addtocart(self):
        Model = input('model #')
        Size = input('Size:  ')
        URL = self.URLGen(Model, float(Size))

        response = session.get(URL, headers={'Upgrade-Insecure-Requests': '1'})
        URL = response.URL
        soup = bs(response.text, 'html.parser')
        size_container = soup.find('select', {'name': Model})
        Size = 'null'

        try:
            for values in size_container.find_all('option'):
                if Size == values.string.strip():
                    Size = values['value']
                    break
        except:
            print('All sold out!')
            return False, 'null', 'null'

        payload = {
            'Quantity': '1',
            'ajax': 'true',
            'layer': 'Add To Bag overlay',
            'masterModel': Model,
            'Model': Size
        }
        headers = {
            'Accept': '*/*',
            'Origin': 'http://www.adidas.com',
            'X-Requested-With': 'XMLHttpRequest'
        }
        if Size != 'null':
            URL = 'http://www.adidas.com' + '/on/demandware.store/Sites-adidas-US-site/en_US/Cart-MiniAddProduct'
            response = session.post(URL, data=payload, headers=headers)
            if response.status_code == 200:
                print('Shoe was added to cart')
                return True, URL, Size
            else:
                print('{} unavailable'.format(Size))
                return False, URL, Size

    addtocart()


    def CheckSizes(url,model):
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit/537.36 (KHTML,like Gecko)Chrome/39.0.2171.95 Safari/537.36'}
        RawHTML = requests.get(url, headers=headers)
        Page = bs4.BeautifulSoup(RawHTML.text, "lxml")
        ListofRawSizes = Page.select('.size-dropdown-block')
        Sizes = str(ListofRawSizes[0].getText()).replace('\t','')
        Sizes = Sizes.replace('\n\n','')
        Sizes = Sizes.split()
        Sizes.remove('Select')
        Sizes.remove('size')
        for size in Sizes:
            print(str(model) + ' Size ' + str(size) + ' Available ')

    def Main(model, size):
        url = model.URLGen(model, size)
        model.CheckSizes(url, model)










