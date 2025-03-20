"""
ImageNet-1K to Taxonomic Families Mapping File
Maps ImageNet synset IDs to five taxonomic families:
- Felidae (cats)
- Canidae (dogs)
- Equidae (horses)
- Bovidae (cattle, sheep, etc.)
- Hippopotamidae (hippos)
"""

IMAGENET_TAXONOMIC_MAPPING = {
    # Felidae (Cats)
    "n02123045": "Felidae",  # tabby cat
    "n02123159": "Felidae",  # tiger cat
    "n02123394": "Felidae",  # Persian cat
    "n02123597": "Felidae",  # Siamese cat
    "n02124075": "Felidae",  # Egyptian cat
    "n02125311": "Felidae",  # cougar, puma
    "n02127052": "Felidae",  # lynx
    "n02128385": "Felidae",  # leopard
    "n02128757": "Felidae",  # snow leopard
    "n02128925": "Felidae",  # jaguar
    "n02129165": "Felidae",  # lion
    "n02129604": "Felidae",  # tiger
    "n02130308": "Felidae",  # cheetah
    
    # Canidae (Dogs)
    "n02085620": "Canidae",  # Chihuahua
    "n02085782": "Canidae",  # Japanese spaniel
    "n02085936": "Canidae",  # Maltese
    "n02086079": "Canidae",  # Pekinese
    "n02086240": "Canidae",  # Shih-Tzu
    "n02086646": "Canidae",  # Blenheim spaniel
    "n02086910": "Canidae",  # papillon
    "n02087046": "Canidae",  # toy terrier
    "n02087394": "Canidae",  # Rhodesian ridgeback
    "n02088094": "Canidae",  # Afghan hound
    "n02088238": "Canidae",  # basset hound
    "n02088364": "Canidae",  # beagle
    "n02088466": "Canidae",  # bloodhound
    "n02088632": "Canidae",  # bluetick
    "n02089078": "Canidae",  # black-and-tan coonhound
    "n02089867": "Canidae",  # Walker hound
    "n02089973": "Canidae",  # English foxhound
    "n02090379": "Canidae",  # redbone
    "n02090622": "Canidae",  # borzoi
    "n02090721": "Canidae",  # Irish wolfhound
    "n02091032": "Canidae",  # Italian greyhound
    "n02091134": "Canidae",  # whippet
    "n02091244": "Canidae",  # Ibizan hound
    "n02091467": "Canidae",  # Norwegian elkhound
    "n02091635": "Canidae",  # otterhound
    "n02091831": "Canidae",  # Saluki
    "n02092002": "Canidae",  # Scottish deerhound
    "n02092339": "Canidae",  # Weimaraner
    "n02093256": "Canidae",  # Staffordshire bullterrier
    "n02093428": "Canidae",  # American Staffordshire terrier
    "n02093647": "Canidae",  # Bedlington terrier
    "n02093754": "Canidae",  # Border terrier
    "n02093859": "Canidae",  # Kerry blue terrier
    "n02093991": "Canidae",  # Irish terrier
    "n02094114": "Canidae",  # Norfolk terrier
    "n02094258": "Canidae",  # Norwich terrier
    "n02094433": "Canidae",  # Yorkshire terrier
    "n02095314": "Canidae",  # wire-haired fox terrier
    "n02095570": "Canidae",  # Lakeland terrier
    "n02095889": "Canidae",  # Sealyham terrier
    "n02096051": "Canidae",  # Airedale
    "n02096177": "Canidae",  # cairn terrier
    "n02096294": "Canidae",  # Australian terrier
    "n02096437": "Canidae",  # Dandie Dinmont terrier
    "n02096585": "Canidae",  # Boston bull
    "n02097047": "Canidae",  # miniature schnauzer
    "n02097130": "Canidae",  # giant schnauzer
    "n02097209": "Canidae",  # standard schnauzer
    "n02097298": "Canidae",  # Scotch terrier
    "n02097474": "Canidae",  # Tibetan terrier
    "n02097658": "Canidae",  # silky terrier
    "n02098105": "Canidae",  # soft-coated wheaten terrier
    "n02098286": "Canidae",  # West Highland white terrier
    "n02098413": "Canidae",  # Lhasa
    "n02099267": "Canidae",  # flat-coated retriever
    "n02099429": "Canidae",  # curly-coated retriever
    "n02099601": "Canidae",  # golden retriever
    "n02099712": "Canidae",  # Labrador retriever
    "n02099849": "Canidae",  # Chesapeake Bay retriever
    "n02100236": "Canidae",  # German short-haired pointer
    "n02100583": "Canidae",  # vizsla
    "n02100735": "Canidae",  # English setter
    "n02100877": "Canidae",  # Irish setter
    "n02101006": "Canidae",  # Gordon setter
    "n02101388": "Canidae",  # Brittany spaniel
    "n02101556": "Canidae",  # clumber spaniel
    "n02102040": "Canidae",  # English springer spaniel
    "n02102177": "Canidae",  # Welsh springer spaniel
    "n02102318": "Canidae",  # cocker spaniel
    "n02102480": "Canidae",  # Sussex spaniel
    "n02102973": "Canidae",  # Irish water spaniel
    "n02104029": "Canidae",  # kuvasz
    "n02104365": "Canidae",  # schipperke
    "n02105056": "Canidae",  # groenendael
    "n02105162": "Canidae",  # malinois
    "n02105251": "Canidae",  # briard
    "n02105412": "Canidae",  # kelpie
    "n02105505": "Canidae",  # komondor
    "n02105641": "Canidae",  # Old English sheepdog
    "n02105855": "Canidae",  # Shetland sheepdog
    "n02106030": "Canidae",  # collie
    "n02106166": "Canidae",  # Border collie
    "n02106382": "Canidae",  # Bouvier des Flandres
    "n02106550": "Canidae",  # Rottweiler
    "n02106662": "Canidae",  # German shepherd
    "n02107142": "Canidae",  # Doberman
    "n02107312": "Canidae",  # miniature pinscher
    "n02107574": "Canidae",  # Greater Swiss Mountain dog
    "n02107683": "Canidae",  # Bernese mountain dog
    "n02107908": "Canidae",  # Appenzeller
    "n02108000": "Canidae",  # EntleBucher
    "n02108089": "Canidae",  # boxer
    "n02108422": "Canidae",  # bull mastiff
    "n02108551": "Canidae",  # Tibetan mastiff
    "n02108915": "Canidae",  # French bulldog
    "n02109047": "Canidae",  # Great Dane
    "n02109525": "Canidae",  # Saint Bernard
    "n02109961": "Canidae",  # Eskimo dog
    "n02110063": "Canidae",  # malamute
    "n02110185": "Canidae",  # Siberian husky
    "n02110341": "Canidae",  # dalmatian
    "n02110627": "Canidae",  # affenpinscher
    "n02110806": "Canidae",  # basenji
    "n02110958": "Canidae",  # pug
    "n02111129": "Canidae",  # Leonberg
    "n02111277": "Canidae",  # Newfoundland
    "n02111500": "Canidae",  # Great Pyrenees
    "n02111889": "Canidae",  # Samoyed
    "n02112018": "Canidae",  # Pomeranian
    "n02112137": "Canidae",  # chow
    "n02112350": "Canidae",  # keeshond
    "n02112706": "Canidae",  # Brabancon griffon
    "n02113023": "Canidae",  # Pembroke Welsh corgi
    "n02113186": "Canidae",  # Cardigan Welsh corgi
    "n02113624": "Canidae",  # toy poodle
    "n02113712": "Canidae",  # miniature poodle
    "n02113799": "Canidae",  # standard poodle
    "n02113978": "Canidae",  # Mexican hairless
    "n02115641": "Canidae",  # dingo
    "n02115913": "Canidae",  # dhole
    "n02116738": "Canidae",  # African hunting dog
    "n02117135": "Canidae",  # hyena
    "n02119022": "Canidae",  # red fox
    "n02119789": "Canidae",  # kit fox
    "n02120079": "Canidae",  # Arctic fox
    "n02120505": "Canidae",  # grey fox
    "n02114367": "Canidae",  # timber wolf
    "n02114548": "Canidae",  # white wolf
    "n02114712": "Canidae",  # red wolf
    "n02114855": "Canidae",  # coyote
    
    # Equidae (Horses)
    "n02389026": "Equidae",  # sorrel
    "n02381460": "Equidae",  # zebra
    "n02389559": "Equidae",  # poncho
    "n02391049": "Equidae",  # zebra
    "n02391994": "Equidae",  # donkey
    "n02397096": "Equidae",  # wild ass
    "n02374451": "Equidae",  # horse
    
    # Bovidae (Cattle, Sheep, etc.)
    "n02415577": "Bovidae",  # bighorn sheep
    "n02417914": "Bovidae",  # ibex
    "n02422106": "Bovidae",  # hartebeest
    "n02422699": "Bovidae",  # impala
    "n02423022": "Bovidae",  # gazelle
    "n02408429": "Bovidae",  # water buffalo
    "n02410509": "Bovidae",  # bison
    "n02412080": "Bovidae",  # ram
    "n02415253": "Bovidae",  # sheep
    "n02417534": "Bovidae",  # goat
    "n02430045": "Bovidae",  # bighorn sheep
    "n02431122": "Bovidae",  # bison
    "n02432983": "Bovidae",  # gnu, wildebeest
    "n01905661": "Bovidae",  # goat
    "n02403003": "Bovidae",  # ox
    "n02402425": "Bovidae",  # cattle
    
    # Hippopotamidae (Hippos)
    "n02398521": "Hippopotamidae",  # hippopotamus
}