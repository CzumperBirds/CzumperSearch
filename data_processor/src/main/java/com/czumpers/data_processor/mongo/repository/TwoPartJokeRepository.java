package com.czumpers.data_processor.mongo.repository;

import com.czumpers.data_processor.mongo.model.TwoPartJokeDTO;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface TwoPartJokeRepository extends MongoRepository<TwoPartJokeDTO, String> {
    Optional<TwoPartJokeDTO> findByJokeId(int jokeId);
}
