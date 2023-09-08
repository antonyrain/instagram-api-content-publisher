import random

my_list = [
    "#3dmodeling", "#digitalart", "#computergraphics", "#3ddesign", "#rendering", "#cad", "#software", "#blender", "#mayacg", "#tips", "#tutorials", "#printing", "#gamedesign", "#visualization", "#productdesign", "#animation", "#virtualreality", "#augmentedreality", "#scanning", "#topology", "#meshediting", "#texturing", "#uvmapping", "#polygonmodeling", "#workflow", "#community",
    "#jewelry3dmodeling", "#jewelrydesign", "#gemstonemodeling", "#customjewelry", "#preciousmetals", "#cad", "#luxuryjewelry", "#bespokejewelry", "#artisanaljewelry", "#handcrafted", "#diamondmodeling", "#gemsetting", "#3dprintingjewelry", "#jewelryprototyping", "#fashionjewelry", "#metalwork", "#jewelrycraftsmanship", "#3ddesign", "#creativejewelry", "#prototypedevelopment",
    "#jewellery", "#fashionjewelry", "#finejewelry", "#handcraftedjewelry", "#luxuryjewelry", "#customjewelry", "#artisanaljewelry", "#jewelrydesign", "#gemstones", "#diamonds", "#preciousmetals", "#jewelrytrends", "#jewelryinspiration", "#jewelrymaking", "#jewelryartistry", "#jewelrylovers", "#jewelryaddict", "#jewelrydesigners", "#jewelryshop",
    "#jewelrybusiness", "#jewelrystore", "#customjewelry", "#finejewelry", "#handcraftedjewelry", "#bespokejewelry", "#jewelrydesigners", "#jewelryshop", "#artisanaljewelry", "#jewelryentrepreneur",
    "#business", "#entrepreneurship", "#smallbusiness", "#startup", "#success", "#leadership", "#management", "#marketing", "#innovation", "#strategy", "#finance", "#entrepreneur", "#growth", "#leadershipdevelopment", "#digitalmarketing", "#entrepreneurlife", "#businessowner", "#worklifebalance", "#businessstrategy",
    "#3dprinting", "#3ddesign", "#3dmodeling", "#3dtechnology", "#3dart", "#3dvisualization", "#3danimation", "#3dgraphics", "#3dmapping", "#3dworld", "#3dprintingcommunity", "#3dprintinglife", "#3dprintingart", "#3dmodelingcommunity", "#3dmodelingart", "#3dartist", "#3drendering", "#3danimationstudio", "#3dprintingtechnology", "#3dprintingdesign",
    "#followme", "#followforfollow", "#followback", "#follow", "#follow4follow", "#followfriday", "#pleasefollow", "#ifollowback", "#followformore",
    "#likeforlike", "#like4like", "#l4l", "#pleaselike", "#doubletap", "#showsomelove", "#hitthatlikebutton", "#givemeLikes", "#likethis",
    "#love", "#instagood", "#photooftheday", "#beautiful", "#happy", "#cute", "#fashion", "#follow", "#like4like", "#tbt", "#picoftheday", "#selfie", "#summer", "#instadaily", "#friends", "#art", "#food", "#style", "#nature", "#fitness",
    "#jewelrymaking", "#handmadejewelry", "#jewelrycrafting", "#diyjewelry", "#jewelrydesign", "#jewelryworkshop", "#beading", "#wirewrapping", "#metalwork", "#gemstonejewelry", "#creativejewelry", "#artisanjewelry", "#crafting", "#jewelryart", "#homemadejewelry", "#jewelrycreations", "#jewelrycraftsmanship", "#jewelryprojects", "#jewelryhobby",
    "#handcraft", "#handmade", "#crafting", "#artisan", "#homemade", "#craftwork", "#diy", "#creativity", "#handcrafted", "#makersgonnamake", "#craftsmanship", "#handmadewithlove", "#crafty", "#handwork", "#creative", "#madewithhands", "#handmadegifts", "#craftersofinstagram", "#crafters", "#artsandcrafts",
    "#creativity", "#creative", "#artistic", "#imagination", "#inspiration", "#innovation", "#creativeprocess", "#thinkoutsidethebox", "#expressyourself", "#creativeideas", "#creativeminds", "#originalartwork", "#creativityflow", "#creativecommunity", "#creativeenergy", "#creativeexpression", "#creativelife", "#creativegenius", "#creativejourney", "#creativityunleashed",
    "#design", "#graphicdesign", "#webdesign", "#interiordesign", "#fashiondesign", "#productdesign", "#architecture", "#industrialdesign", "#designinspiration", "#creative", "#designthinking", "#artanddesign", "#digitaldesign", "#designerlife", "#designstudio", "#designprocess", "#designers", "#designcommunity", "#visualdesign", "#designideas",
    "#art", "#artistic", "#fineart", "#visualart", "#contemporaryart", "#creative", "#painting", "#drawing", "#sculpture", "#mixedmedia", "#artgallery", "#artwork", "#artlovers", "#modernart", "#abstractart", "#digitalart", "#artistsoninstagram", "#artworld", "#artislife", "#artisticexpression",
    "#silverjewelry", "#silveraccessories", "#sterlingsilver", "#handmadesilver", "#silverjewellery", "#silvercraft", "#silversmithing", "#silverdesign", "#silverwork", "#silverart", "#silverstyle", "#silverbeauty", "#silverfashion", "#silverdesigner", "#silverartistry", "#artisanalsilver", "#silversmith", "#silvercreations", "#uniquejewelry", "#elegantjewelry",
    "#goldjewelry", "#goldaccessories", "#finegold", "#handmadegold", "#goldjewellery", "#goldcraft", "#goldsmithing", "#golddesign", "#goldwork", "#goldart", "#goldstyle", "#goldbeauty", "#goldfashion", "#golddesigner", "#goldartistry", "#artisangold", "#goldsmith", "#goldcreations", "#luxuryjewelry", "#elegantjewelry",
    "#lifestyle", "#healthychoices", "#wellness", "#fitnessjourney", "#balancedlife", "#livelife", "#mindfulness", "#selfcare", "#happiness", "#positivemindset", "#lifeisbeautiful", "#wellbeing", "#healthyliving", "#luxurylife", "#simpleliving", "#adventurouslife", "#lifegoals", "#lovelife", "#stressfree", "#gratitude",
    "#style", "#fashion", "#trendy", "#outfitoftheday", "#streetstyle", "#chic", "#stylish", "#fashionista", "#ootd", "#styleinspiration", "#instafashion", "#fashionlover", "#fashionforward", "#styleguide", "#fashionable", "#elegance", "#modernstyle", "#casualstyle", "#classy",
    "#urbanlife", "#cityliving", "#metropolitan", "#cityscape", "#urbanexploration", "#cityvibes", "#urbanadventures", "#citylights", "#citylifestyle", "#citydwellers", "#urbanexperience", "#cityculture", "#urbanstyle", "#citylife", "#downtownliving", "#citylovers", "#cityview", "#streetlife", "#urbanjungle",
    "#photography", "#photographer", "#photographyskills", "#photographylovers", "#photooftheday", "#capturedmoments", "#beautifulshots", "#pictureperfect", "#cameralife", "#creativeshot", "#focusandshoot", "#photographyart", "#shutterbug", "#visualstorytelling", "#snapshot", "#photoaddict", "#instaphotography", "#travelphotography", "#portraitphotography", "#landscapephotography"
]


def random_tags():
    random_set = set()
    it = 0
    while it < 29:
        r = random.randint(0, len(my_list)-1)
        random_set.add(my_list[r])
        it += 1

    hashtags_string = ' '.join(random_set)
    
    return hashtags_string
