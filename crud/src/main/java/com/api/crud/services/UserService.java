package com.api.crud.services;


import com.api.crud.models.UserModel;
import com.api.crud.repository.IUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import javax.swing.text.html.Option;
import java.util.ArrayList;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    IUserRepository iUserRepository;
    public ArrayList<UserModel> getUser(){
        return (ArrayList<UserModel>) iUserRepository.findAll();
    }

    public UserModel SaveUser(UserModel user){
        return iUserRepository.save(user);
    }

    public Optional<UserModel> FindById(Long id){
        return this.iUserRepository.findById(id);
    }

    public UserModel UpdateById(UserModel request, Long id){
        UserModel user = iUserRepository.findById(id).get();

        user.setFirstname(request.getFirstname());
        user.setLastname(request.getLastname());
        user.setEmail(request.getEmail());

        return user;
    }

    public Boolean DeleteUser(Long id){
        try {
            iUserRepository.deleteById(id);
            return true;
        }catch (Exception e){
            return false;
        }
    }


}
