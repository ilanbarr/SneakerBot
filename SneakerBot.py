import requests
import random
import webbrowser
import bs4
import mechanicalsoup
<<<<<<< HEAD

=======
import random
>>>>>>> a5ca02c68f84120097f7966fa5d2de4672b3bb06


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

<<<<<<< HEAD
    def CheckSizes(URL,model):
        print('checking sizes...')
=======


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

    def CheckSizes(url,model):
>>>>>>> a5ca02c68f84120097f7966fa5d2de4672b3bb06
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

<<<<<<< HEAD
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
=======
    def Main(model, size):
        url = model.URLGen(model, size)
        model.CheckSizes(url, model)
        url = URLGen(model, size)
        CheckSizes(url, model)
>>>>>>> a5ca02c68f84120097f7966fa5d2de4672b3bb06

    #Model = input('model #')
    #Size = input('Size:  ')
    #URL = URLGen(Model,float(Size))
    #print(str(URL))
    #addtocart()

    #mechanical soup tutorial
    #browser = mechanicalsoup.StatefulBrowser()
    #browser.open("http://httpbin.org/")
    #browser.follow_link("forms")
    #print(browser.get_url())

    #browser3 = mechanicalsoup.StatefulBrowser()
    #browser3.open("http://www.google.com/")
    #imagesLink = browser3.links().pop(0)
    #browser3.follow_link(imagesLink)
    #browser3.select_form()
    #form = browser3.get_current_form()
    #print(form.print_summary())
    #form.set("q", "Guinea Pig")
    #form.choose_submit('btnG')
    #browser3.submit_selected()
    #print(browser3.get_url())
    #gpPics = browser3.links()
    #print(gpPics)
    #browser3.follow_link(gpPics.pop(0))
    #print(browser3.get_url())

    browser2 = mechanicalsoup.StatefulBrowser()
    browser2.open("https://www.nike.com/t/air-huarache-mens-shoe-eoToq9X2")
    soup = browser2.get_current_page()
    #print(soup)
    #print(soup.find_all('gnav'))
    browser2.select_form()
    form = browser2.get_current_form()
    print(form.print_summary())
    Model = input('model #')
    form.set("search", Model)
    form.choose_submit(form.)
    #browser2.submit_selected()
    browser2.submit(form)
    print(browser2.get_url())




    #print(browser2.list_links())