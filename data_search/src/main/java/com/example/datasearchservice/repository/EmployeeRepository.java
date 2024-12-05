package com.example.datasearchservice.repository;

import com.example.datasearchservice.model.Employee;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

public interface EmployeeRepository extends ElasticsearchRepository<Employee, String> {
    List<Employee> findByFirstNameContaining(String firstName);
}
