import twitter_module as tm
import insta_module as im
import you_module as ym
import patreon_module as pm

def get_data_from_links(driver):
    smlinks = pm.get_links()
    for smlink in smlinks:
        if 'insta' in smlink:
            im.get_data_from_instagram(driver, smlink)
            print('-----instagram is done-----')
        elif 'twit' in smlink:
            tm.get_data_from_twitter(driver, smlink)
            print('-----twitter is done------')
        elif 'you' in smlink:
            ym.get_data_from_youtube(driver, smlink)
            print('-----youtube is done------')
    return