import unittest

from crm.automatedtests.customer import AddCustomer, EditCustomerDetails, ViewCustomerSummary, ExportCustomerSummary, \
    CustomerDetails, DeleteCustomerSummary
from crm.automatedtests.products import AddProduct, EditProductDetails, ViewProductSummary, ExportProductSummary, \
    ProductDetails, DeleteProductSummary
from crm.automatedtests.services import AddService, EditServiceDetails, ViewServiceSummary, ServiceDetails, \
    DeleteService


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(AddCustomer))
suite.addTest(loader.loadTestsFromModule(CustomerDetails))
suite.addTest(loader.loadTestsFromModule(EditCustomerDetails))
suite.addTest(loader.loadTestsFromModule(ViewCustomerSummary))
suite.addTest(loader.loadTestsFromModule(ExportCustomerSummary))
suite.addTest(loader.loadTestsFromModule(AddProduct))
suite.addTest(loader.loadTestsFromModule(ProductDetails))
suite.addTest(loader.loadTestsFromModule(EditProductDetails))
suite.addTest(loader.loadTestsFromModule(ViewProductSummary))
suite.addTest(loader.loadTestsFromModule(ExportProductSummary))
suite.addTest(loader.loadTestsFromModule(AddService))
suite.addTest(loader.loadTestsFromModule(ServiceDetails))
suite.addTest(loader.loadTestsFromModule(EditServiceDetails))
suite.addTest(loader.loadTestsFromModule(ViewServiceSummary))
suite.addTest(loader.loadTestsFromModule(DeleteCustomerSummary))



runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

