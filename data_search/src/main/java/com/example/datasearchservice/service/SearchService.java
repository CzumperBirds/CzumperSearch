package com.example.datasearchservice.service;

import com.example.datasearchservice.model.Employee;
import com.example.datasearchservice.repository.EmployeeRepository;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class SearchService {
    private final EmployeeRepository repository;

    public SearchService(EmployeeRepository repository) {
        this.repository = repository;
    }

    public List<Employee> search(String searchPhrase) {
        return repository.findByFirstNameContaining(searchPhrase);
    }
}
