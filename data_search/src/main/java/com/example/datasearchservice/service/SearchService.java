package com.example.datasearchservice.service;

import com.example.datasearchservice.entity.Employee;
import com.example.datasearchservice.repository.EmployeeRepository;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class SearchService {
    private final EmployeeRepository repository;

    public SearchService(EmployeeRepository repository) {
        this.repository = repository;
    }

    @Cacheable(value = "employees", key = "#firstName")
    public List<Employee> search(String firstName) {
        return repository.findByFirstNameContaining(firstName);
    }
}
