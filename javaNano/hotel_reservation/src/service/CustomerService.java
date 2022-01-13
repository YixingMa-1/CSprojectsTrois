package service;

import model.Customer;

import java.util.ArrayList;
import java.util.Collection;

public class CustomerService {
    // provide a static reference
    private static CustomerService customerService = null;
    private static Collection<Customer> customers;
    private CustomerService() {
        this.customers = new ArrayList<>();
    }

    public static CustomerService getInstance() {
        if (customerService == null) {
            customerService = new CustomerService();
        }
        return customerService;
    }

    public static void addCustomer(String email, String firstName, String lastName) throws IllegalArgumentException{
        customers.add(new Customer(firstName, lastName, email));
    }

    public Customer getCustomer(String customerEmail){
        for (Customer customer: customers) {
            if (customer.getEmail().equals(customerEmail)) {
                return customer;
            }
        }
        return null;
    }

    public Collection<Customer> getAllCustomers() { return customers;}
}
