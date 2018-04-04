
@pytest.fixture()
def fxt(request):

    print("IN fixture")
    
    def fin():

        print("IN fin")

    request.addfinalizer(fin)

    return lib.div

