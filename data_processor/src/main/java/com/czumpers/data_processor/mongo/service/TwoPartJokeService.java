package com.czumpers.data_processor.mongo.service;

import com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed;
import com.czumpers.data_processor.mongo.model.TwoPartJokeDTO;
import com.czumpers.data_processor.mongo.repository.TwoPartJokeRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class TwoPartJokeService {
    private final TwoPartJokeRepository twoPartJokeRepository;

    public boolean isNewJoke(TwoPartJokeConsumed joke) {
        return twoPartJokeRepository.findByJokeId(joke.getId()).isEmpty();
    }

    public void saveJoke(TwoPartJokeConsumed joke) {
        twoPartJokeRepository.save(new TwoPartJokeDTO(joke.getId()));
    }
}
