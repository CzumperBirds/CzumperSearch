package com.czumpers.data_processor.mongo.repository;

import com.czumpers.data_processor.mongo.model.OnePartJokeDTO;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface OnePartJokeRepository extends MongoRepository<OnePartJokeDTO, String> {
    Optional<OnePartJokeDTO> findByJokeId(int jokeId);
}
