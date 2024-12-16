package com.example.datasearchservice.repository;

import com.example.datasearchservice.entity.Employee;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

@CacheConfig(cacheNames = "employees")
public interface EmployeeRepository extends ElasticsearchRepository<Employee, String> {
    List<Employee> findByFirstNameContaining(String firstName);
}
